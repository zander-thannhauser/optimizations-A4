
from sys import argv;

from heapq import heappop, heappush;

from instruction.self import instruction;

from block.self import block;

from read_block import read_block;

from expression_table.self import expression_table;
from expression_table.parameter.self import parameter;

from phases.lost_parent.self           import lost_parent_phase;
from phases.reset_dominators.self      import reset_dominators_phase;
from phases.dominators.self            import dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;
from phases.post_dominators.self       import post_dominators_phase;
from phases.in_out.self                import in_out_phase;
from phases.inheritance.self           import inheritance_phase;
from phases.phi.self                   import phi_phase;
from phases.optimize.self              import optimize_phase;
from phases.superfical_critical.self   import superfical_critical_phase;
from phases.dead_code.self             import dead_code_phase;

from phases.valnum_singleton_sets.self     import valnum_singleton_sets_phase;
from phases.union_valnum_sets.self         import union_valnum_sets_phase;
from phases.rename_valnums_to_liveids.self import rename_valnums_to_liveids_phase;

from phases.live_in_out.self      import live_in_out_phase;
from phases.live_inheritance.self import live_inheritance_phase;
from phases.live_instances.self   import live_instances_phase;

# dead code removal:
#from phases.dead_code.self             import dead_code_phase;

# register allocation:

from debug import *;

def setup_start_block(t, p, et):
	assert(t.token == ".frame");
	
	name = next(t);
	assert(next(t) == ',');
	framesize = next(t);
	
	vr_args = [];
	vn_args = [];
	parameters = [];
	
	while next(t) == ",":
		reg = next(t);
		vr_args.append(reg);
	
	givens = ["%vr0", "%vr1", "%vr2", "%vr3"] + vr_args;
	
	for register in givens:
		param = parameter(register);
		valnum = et.extovn(param);
		vn_args.append(valnum);
		parameters.append(param);
	
	p.printf(".frame %s, %s %s", name, framesize, \
		"".join(f", %vr{vn}" for vn in vn_args[4:]), prefix = "");
	
	start = block(".frame", [], ["(fallthrough)"]);
	
	start.vn_args = vn_args;
	
	return start, parameters;

def setup_end_block():
	ret = instruction("ret", [], []);
	end = block(".return", [], [], ret);
	return end;

def read_all_blocks(t, start, end):
	all_blocks = [];
	
	all_blocks.append(start);
	
	while t.token and t.token != ".frame":
		b = read_block(t);
		all_blocks.append(b);
	
	all_blocks.append(end);
	
	return all_blocks;

def resolve_references(all_blocks):
	enter("resolve_references()");
	
	blocks_by_name = {};
	
	for b in all_blocks:
		if b.label:
			blocks_by_name[b.label] = b;
	
	for i, b in enumerate(all_blocks):
		successors = [];
		
		dprint(f"i = {i}");
		dprint(f"b.label = {b.label}");
		dprint(f"b.children_labels = {b.children_labels}");
		
		for c in b.children_labels:
			if c == "(fallthrough)":
				successors.append(all_blocks[i + 1]);
			elif c in blocks_by_name:
				successors.append(blocks_by_name[c]);
			else:
				fprintf(stderr, "%s: unresolved reference to '%s'!\n", argv[0], c);
				sys.exit(1);
		
		for c in successors:
			c.predecessors.append(b);
		b.successors = successors;
	
	exit("return;");

def postorder_rank(b, x):
	if b.po: return x;
	b.po = 1;
	for c in b.successors: x = postorder_rank(c, x);
	b.po = x;
	x += 1;
	return x;

def reverse_postorder_rank(b, x, n):
	if b.rpo: return x;
	b.rpo = 1;
	for c in b.predecessors: x = reverse_postorder_rank(c, x, n);
	b.rpo = x;
	b.hue = (x - 1) / n;
	x += 1;
	return x;

def process_frame(t, p):
	
	enter("process_frame");
	
	et = expression_table();
	
	instruction.counter = 0;
	
	start, parameters = setup_start_block(t, p, et);
	
	end = setup_end_block();
	
	all_blocks = read_all_blocks(t, start, end);
	
	resolve_references(all_blocks);
	
	postorder_rank(start, 1);
	
	reverse_postorder_rank(end, 1, len(all_blocks));
	
	todo = [
		# call lost_parent_phase on all blocks:
		lost_parent_phase(block) for block in all_blocks
	] + [
		reset_dominators_phase(start),      # top-down*
		dominators_phase(start),            # top-down
		reset_post_dominators_phase(end),   # bottom-up*
		post_dominators_phase(end),         # bottom-up
		## reset_in_out_phase(end),         # bottom-up
		in_out_phase(end),                  # bottom-up
		inheritance_phase(start),           # top-down
		phi_phase(start),                   # top-down*
		optimize_phase(start),              # top-down
		
		superfical_critical_phase(start),   # top-down
		## critical(),  # bottom-up
		dead_code_phase(start),             # top-down*
		
		valnum_singleton_sets_phase(start), # top-down*:
			# create singleton sets of each valnum used/defined
			# create mapping valnum -> valnum-set
		
		union_valnum_sets_phase(start), # top-down*:
			# for every phi node: get the valnums that feed it
			# get the sets of those valnums
			# union them togteher
			# update mapping
		
		rename_valnums_to_liveids_phase(start), # top-down:
			# assign valnum-sets live range ids
			# rename all valnums to the live-range id
		
		# repeat point:
		
		live_in_out_phase(end), # bottom-up:
			# ids used but not defined in this block
			# ids defined and set([last instruction that defined it])
			# defines -> set of unique numbers (instruction id?)
				# (initalized to singltions)
		
		live_inheritance_phase(start), # top-down:
			# pass downwards a set of live-range id -> set of definers
			# every live-in:
				# if there's more than one definer:
					# union all their definers-sets together
					# update the mapping
			# every live-out:
				# sets the downwards-dict make to the singleton
		
		live_instances_phase(start), # top-down*:
			# create dict(): define-sets -> liverange instances
			# for every instruction:
				# if it's a usage:
					# store in it the instance it should introduce
				# if you see a define:
					# lookup mapping, create if None
					# update mapping with define's instance
			# pass downwards a liverange id -> instance
			# the bottom of every block should remember outgoing mapping
		
		# bottom-up: build_interference
			# recall above outgoing mapping
			# for every instruction[::-1]:
				# if you see a definition:
					# remove instance from mapping
					# mark this instance as iterfering with
					# all other instances in current mapping
					# calculate cost
				# if you see a usage:
					# introduce instance into mapping
		
		# assign live range to register:
			# if possible: push to rename phase
			# otherwise: push to spill-over phase
		
		# spill-over phase:
			# given a live-range, insert loads and stores
			# invoke live-range in/out reset on start again.
		
		# rename phase:
			# if this live range is of the current (last) batch
			# rename uses and defintions and remove `i2i same -> same`s
	];
	
	args = {
		"all_blocks": all_blocks,
		
		"start": start,
		
		"end": end,
		
		"parameters": parameters,
		
		"expression_table": et,
		
		"valnum_to_vnsets": dict(), # valnum -> set of valnums
		
		"vnsets_to_liveid": {
			# set of valnums -> live id (integer)
			"next": 0
		},
		
		"defineset_to_liverange": dict(), # set of instructions -> liverange
		
		"phis": set(), # phi expressions
		
		"all_liveranges": set(),
		
		"phase_counters": {
			"superfical-critical": 1,
			"dead-code": 1,
			"valnum_singleton_sets": 1,
			"union_valnum_sets": 1,
			"rename_valnums_to_liveids": 1,
		},
	};
	
	if len(todo):
		todo[0].dotout(**args);
	
	while len(todo):
		# print([str(p) for p in todo]);
		phase = heappop(todo);
		addmes = phase.process(**args);
		phase.dotout(**args);
		for me in addmes:
			if me not in todo:
				heappush(todo, me);
	
#	p.indent();
#	print_asm(start, p);
#	p.unindent();
	
	exit("process_frame");
	

































