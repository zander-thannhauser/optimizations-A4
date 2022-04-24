
from debug import *;

from phases.union_valnum_sets.self import union_valnum_sets_phase;

def union_valnum_sets_phase_process(self, end, phis, valnum_to_vnsets, expression_table, phase_counters, **_):
	enter(f"union_valnum_sets.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	for phi_valnum in block.incoming_phis.values():
		phi = expression_table.vntoex(phi_valnum);
		phis.add(phi);
	
	if block == end:
		
		dprint(f"phis = {[str(p) for p in phis]}")
		
		regtophis = dict() # virtual register -> set of phis
		
		for p in phis:
			regtophis.setdefault(p.register, set()).add(p);
		
		dprint(f"regtophis = {regtophis}")
		
		for reg, phis in regtophis.items():
			if len(phis) > 1:
				union = set();
				for p in phis:
					union.update(valnum_to_vnsets[p.valnum]);
				for me in union:
					valnum_to_vnsets[me] = union;
		
	else:
		block.phase_counters["union_valnum_sets"] = phase_counters["union_valnum_sets"]
	
		for child in block.successors:
			if child.phase_counters["union_valnum_sets"] < phase_counters["union_valnum_sets"]:
				todo.append(union_valnum_sets_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















