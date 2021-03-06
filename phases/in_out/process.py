
from debug import *;

from phases.in_out.self import in_out_phase;

def in_out_phase_process(self, start, parameters, **_):
	enter(f"in_out_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	ins = set();
	outs = list();
	
	# union children's needs
	for child in block.successors:
		if child.ins is not None:
			ins.update(child.ins);
	
	todo = [];
	
	dprint(f"ins = {ins}");
	dprint(f"outs = {outs}");
	
	# the last instruction might need something too (conditional branch):
	if block.jump:
		ins.update(block.jump.ins);
	
	new_instructions = [];
	
	for inst in block.original_instructions[::-1]:
		dprint(f"inst = {inst}");
		
		if (inst.out in ins) or inst.op in \
				["iwrite", "iread", "store", "assert", "ret", "swrite", "call", "putchar"]:
			# (either it's useful or protected)
			
			# is it publishing something?
			if inst.out is not None and inst.out not in outs:
				outs.insert(0, inst.out);
			
			ins.discard(inst.out);
			ins.update(inst.ins);
			
			new_instructions.insert(0, inst);
		elif inst.op not in ["add", "i2i", "loadI", "testge", "testgt", "testle", "comp", "load"]:
			assert(not "TODO");
	
	block.instructions = new_instructions;
	
	if block == start:
		# I'm the start block
		# so I should look like I produce the parameter's registers:
		
		outs = [p.register for p in parameters];
		
		ins.difference_update(outs);
		
		if len(ins):
			dprint(f"ins = {ins}")
			assert(not "undefined register used!");
	
	dprint(f"ins = {ins}, outs = {outs}");
	
	if block.ins != ins:
		for parent in block.predecessors:
			todo.append(in_out_phase(parent));
		block.ins = ins;
		
	block.ins = ins;
	block.outs = outs;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















