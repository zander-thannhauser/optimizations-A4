
from debug import *;

from phases.live_in_out.self import live_in_out_phase;

def live_in_out_phase_process(self, start, parameters, **_):
	enter(f"live_in_out_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	ins = set();
	outs = dict(); # live-range id -> instruction
	
	# union children's needs
	for child in block.successors:
		if child.live_ins is not None:
			ins.update(child.live_ins);
	
	todo = [];
	
	dprint(f"ins = {ins}");
	dprint(f"outs = {outs}");
	
	# the last instruction might need something too (conditional branch):
	if block.newer_jump:
		ins.update(block.newer_jump.ins);
	
	for inst in block.newer_instructions[::-1]:
		dprint(f"inst = {inst}");
		
		# is it publishing something?
		if inst.out is not None:
			inst.define_set = set([inst]);
			if inst.out not in outs:
				outs[inst.out] = inst;
		
		ins.discard(inst.out);
		ins.update(inst.ins);
		
	dprint(f"ins = {ins}");
	dprint(f"outs = {outs}");
		
	if block == start:
		# I'm the start block
		# so I should look like I produce the parameter's registers:
		
		for p in parameters:
			outs[p.liveid] = None;
			ins.discard(p.liveid);
		
		if len(ins):
			dprint(f"ins = {ins}")
			assert(not "undefined register used!");
	
	dprint(f"ins = {ins}, outs = {outs}");
	
	if block.live_ins != ins:
		for parent in block.predecessors:
			todo.append(live_in_out_phase(parent));
		block.live_ins = ins;
		
	block.live_ins = ins;
	block.live_outs = outs;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















