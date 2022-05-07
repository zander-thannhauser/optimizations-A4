
from debug import *;

from phases.in_out.self import in_out_phase;
from phases.inheritance.self import inheritance_phase;

def in_out_phase_process(self, start, parameters, **_):
	enter(f"in_out_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	ins = set();
	loc = set();
	outs = list();
	
	# union children's needs
	for child in block.successors:
		if child.ins is not None:
			ins.update(child.ins);
	
	todo = [];
	
	dprint(f"ins = {ins}");
	dprint(f"loc = {loc}");
	dprint(f"outs = {outs}");
	
	# the last instruction might need something too (conditional branch):
	if block.jump:
		loc.update(block.jump.ins);
	
	for inst in block.original_instructions[::-1]:
		dprint(f"inst = {inst}");
		
		# is it publishing something?
		if inst.out is not None and inst.out not in outs:
			outs.insert(0, inst.out);
		
		loc.discard(inst.out);
		loc.update(inst.ins);

	if block == start:
		# I'm the start block
		# so I should look like I produce the parameter's registers:
		
		outs = [p.register for p in parameters];
		
		ins.difference_update(outs);
		
		if len(ins):
			dprint(f"ins = {ins}")
			assert(not "undefined register used!");
	
	ins.difference_update(outs);
	ins.update(loc);
	
	dprint(f"ins = {ins}");
	dprint(f"loc = {loc}");
	dprint(f"outs = {outs}");
	
	if block.ins != ins:
		for parent in block.predecessors:
			todo.append(in_out_phase(parent));
		todo.append(inheritance_phase(block));
	
	if block.outs != outs:
		for child in block.successors:
			todo.append(inheritance_phase(child));
	
	block.ins = ins;
	block.loc = loc;
	block.outs = outs;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















