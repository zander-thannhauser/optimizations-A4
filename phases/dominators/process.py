
from debug import *;

from phases.optimize.self import optimize_phase;
from phases.dominators.self import dominators_phase;

def dominators_phase_process(self, all_blocks, **_):
	enter(f"dominators_phase_process(block.po = {self.block.po})");
	
	block = self.block;
	
	match len(block.predecessors):
		case 0:
			dominators = set();
			immediate_dominator = None;
		case 1:
			parent, = block.predecessors;
			dominators = parent.dominators.copy();
			immediate_dominator = parent;
		case _:
			predecessors_dominators = [p.dominators for p in block.predecessors];
			dominators = set.intersection(*predecessors_dominators);
			immediate_dominator = min(dominators, key = lambda b: b.po);
	
	dominators.add(block);
	
	dprint(f"dominators = {[str(d) for d in dominators]}")
	
	todo = [];
	
	if block.immediate_dominator != immediate_dominator:
		todo.append(optimize_phase(block));
		block.immediate_dominator = immediate_dominator;
	
	if block.dominators != dominators:
		for successor in block.successors:
			todo.append(dominators_phase(successor));
		block.dominators = dominators;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















