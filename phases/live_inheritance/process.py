
from debug import *;

from phases.phi.self import phi_phase;
from phases.live_inheritance.self import live_inheritance_phase;

def live_inheritance_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"live_inheritance_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	given = dict();
	
	todo = [];
	
	dprint(f"block.ins = {block.ins}")
	
	for predecessor in block.predecessors:
		if predecessor.live_given is not None:
			giving = predecessor.live_given.copy();
			
			for reg, inst in predecessor.live_outs.items():
				dprint(f"inst = {inst}")
				if inst is None: # (parameter):
					giving[reg] = set();
				else:
					giving[reg] = set([inst]);
			
			dprint(f"{predecessor}.giving = {[str(g) for g in giving]}");
			
			for register in block.live_ins:
				assert(register in giving);
				original = given.setdefault(register, set());
				more = giving[register];
				original.update(more);
				for o in original:
					o.define_set = original;
	
	dprint(f"given = {given}");
	
	if block.live_given != given:
		for successor in block.successors:
			todo.append(live_inheritance_phase(successor));
		block.live_given = given;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















