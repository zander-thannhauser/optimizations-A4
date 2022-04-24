
from debug import *;

from phases.valnum_singleton_sets.self import valnum_singleton_sets_phase;

def valnum_singleton_sets_phase_process(self, start, parameters, valnum_to_vnsets, phase_counters, **_):
	enter(f"valnum_singleton_sets.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	if block == start:
		for p in parameters:
			valnum_to_vnsets[p.valnum] = set([p.valnum]);
	
	for inst in block.new_instructions:
		if inst.out is not None and inst.out not in valnum_to_vnsets:
			valnum_to_vnsets[inst.out] = set([inst.out]);
	
	block.phase_counters["valnum_singleton_sets"] = phase_counters["valnum_singleton_sets"]
	
	for child in block.successors:
		if child.phase_counters["valnum_singleton_sets"] < phase_counters["valnum_singleton_sets"]:
			todo.append(valnum_singleton_sets_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















