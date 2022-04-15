
from debug import *;

from phases.reset_dominators.self import reset_dominators_phase;
from phases.dominators.self import dominators_phase;

def reset_dominators_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"reset_dominators_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	block.dominators = set(all_blocks);
	
	todo.append(dominators_phase(block));
	
	block.phase_counters["reset-dominators"] = phase_counters["reset-dominators"];
	
	for child in block.successors:
		if child.phase_counters["reset-dominators"] < phase_counters["reset-dominators"]:
			todo.append(reset_dominators_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















