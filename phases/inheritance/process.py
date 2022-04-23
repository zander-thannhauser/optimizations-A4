
from debug import *;

from phases.phi.self import phi_phase;
from phases.inheritance.self import inheritance_phase;

def inheritance_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"inheritance_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	given = dict();
	
	todo = [];
	
	dprint(f"block.ins = {block.ins}")
	
	for predecessor in block.predecessors:
		if predecessor.given is not None:
			giving = predecessor.given.copy();
			
			for reg in predecessor.outs:
				giving[reg] = set([predecessor]);
			
			dprint(f"{predecessor}.giving = {giving}");
			
			for register in block.ins:
				assert(register in giving);
				given.setdefault(register, set()).update(giving[register]);
	
	dprint(f"given = {given}");
	
	if block.given != given:
		todo.append(phi_phase(block));
		for successor in block.successors:
			todo.append(inheritance_phase(successor));
		block.given = given;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















