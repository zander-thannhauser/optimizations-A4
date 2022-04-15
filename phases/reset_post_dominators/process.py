
from debug import *;

from phases.post_dominators.self import post_dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;

def reset_post_dominators_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"reset_post_dominators_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	block.post_dominators = set(all_blocks);
	
	todo.append(post_dominators_phase(block));
	
	block.phase_counters["reset-post-dominators"] = phase_counters["reset-post-dominators"];
	
	for parent in block.predecessors:
		if parent.phase_counters["reset-post-dominators"] < phase_counters["reset-post-dominators"]:
			todo.append(reset_post_dominators_phase(parent));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















