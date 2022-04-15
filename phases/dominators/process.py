
from debug import *;

from phases.dominators.self import dominators_phase;

def dominators_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"dominators_phase_process(block.po = {self.block.po})");
	
	block = self.block;
	
	match len(block.predecessors):
		case 0:
			dominators = set();
		case 1:
			parent, = block.predecessors;
			dominators = parent.dominators.copy();
			block.immediate_dominator = parent;
		case _:
			predecessors_dominators = [p.dominators for p in block.predecessors];
			dominators = set.intersection(*predecessors_dominators);
			block.immediate_dominator = min(dominators, key = lambda b: b.po);
	
	dominators.add(block)
	
	dprint(f"dominators = {[str(d) for d in dominators]}")
	
	todo = [];
	
	if block.dominators != dominators:
		for successor in block.successors:
			todo.append(dominators_phase(successor));
		block.dominators = dominators;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















