
from debug import *;

from phases.phi.self import phi_phase;
from phases.live_instances.self import live_instances_phase;
from phases.live_inheritance.self import live_inheritance_phase;

def live_inheritance_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"live_inheritance_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	given = dict();
	
	todo = [];
	
	dprint(f"block.live_ins = {block.live_ins}")
	
	for predecessor in block.predecessors:
		if predecessor.live_given is not None:
			giving = predecessor.live_given.copy();
			
			for reg, inst in predecessor.live_outs.items():
				if inst is None: # (parameter):
					giving[reg] = set();
				else:
					dprint(f"inst = {inst}")
					giving[reg] = set([inst]);
			
			dprint(f"{predecessor}.giving = {[str(g) for g in giving]}");
			
			for register in block.live_ins:
				assert(register in giving);
				original = given.get(register, set());
				dprint(f"giving[register] = {giving[register]}")
				if len(giving[register]):
					more = set.union(*(x.define_set for x in giving[register]));
				else:
					more = dict();
				new = set.union(original, more);
				for o in new:
					o.define_set = new;
				given[register] = new;
	
	dprint(f"given = {given}");
	
	if block.live_given != given:
		todo.append(live_instances_phase(block));
		for successor in block.successors:
			todo.append(live_inheritance_phase(successor));
		block.live_given = given;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















