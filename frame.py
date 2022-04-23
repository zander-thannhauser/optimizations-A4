
from sys import argv;

from heapq import heappop, heappush;

from instruction.self import instruction;

from block.self import block;

from read_block import read_block;

from expression_table.self import expression_table;
from expression_table.parameter.self import parameter;

# code motion:
from phases.lost_parent.self           import lost_parent_phase;
from phases.syntax_lookup.self         import syntax_lookup_phase;
from phases.available.self             import available_phase;
from phases.anticipation.self          import anticipation_phase;
from phases.earliest.self              import earliest_phase;
from phases.later.self                 import later_phase;
from phases.insert_delete.self         import insert_delete_phase;

# SSA redundancy elimination:
#from phases.reset_dominators.self      import reset_dominators_phase;
#from phases.dominators.self            import dominators_phase;
#from phases.reset_post_dominators.self import reset_post_dominators_phase;
#from phases.post_dominators.self       import post_dominators_phase;
#from phases.in_out.self                import in_out_phase;
#from phases.inheritance.self           import inheritance_phase;
#from phases.phi.self                   import phi_phase;
#from phases.optimize.self              import optimize_phase;

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
	print(f"b.po[0] = {b.po[0]}");
	if b.po[0]: return x;
	b.po = (1, 0);
	for c in b.successors: x = postorder_rank(c, x);
	b.po = (x, 0);
	print(f"b.po[0] = {b.po[0]}");
	x += 1;
	return x;

def reverse_postorder_rank(b, x, n):
	if b.rpo[0]: return x;
	b.rpo = (1, 0);
	for c in b.predecessors: x = reverse_postorder_rank(c, x, n);
	b.rpo = (x, 0);
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
		# Code Motion (A3):
		syntax_lookup_phase(start), # top-down
		available_phase(start),     # top-down
		anticipation_phase(end),    # bottom-up
		earliest_phase(start),      # top-down
		later_phase(start),         # top-down
		insert_delete_phase(start), # top-down
		
		# SSA redundancy elimination (A2):
#		reset_dominators_phase(start),    # top-down*
#		dominators_phase(start),          # top-down
#		reset_post_dominators_phase(end), # bottom-up*
#		post_dominators_phase(end),       # bottom-up
#		## reset_in_out_phase(end),       # bottom-up
#		in_out_phase(end),                # bottom-up
#		inheritance_phase(start),         # top-down
#		phi_phase(start),                 # top-down*
#		optimize_phase(start),            # top-down
		
		# A3?:
		# superfical_cruciality(start)
		# critical(),  # bottom-up
			# sort by instruction rpo
		# dead_code_phase(start),           # top-down*
		
		# find all still-alive phis, assign them live-range ids.
		
		# A4:
		## reset live-range in-out # top-down
		# live-range in-out        # bottom-up
		# build_interference       # bottom-up
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
		
		"syntax_lookup": dict(), # destination -> instruction
		
		"usage": dict(), # this valnum is used by -> these valnums (kill them)
		
		"earliest": dict(), # (p, s) -> set of instructions
		
		"later": dict(), # (p, s) -> set of instructions
		
		"insert": dict(), # (p, s) -> set of instructions
		
#		"expression_table": et,
#		
#		"parameters": parameters,
#		
#		"phis": list(),
		
		"phase_counters": {
			"syntax-lookup": 1,
			"earliest": 1,
			"insert-delete": 1,
			"dead-code": 1,
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
	

































