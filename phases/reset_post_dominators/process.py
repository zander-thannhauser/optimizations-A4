
from debug import *;

from phases.post_dominators.self import post_dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;

def reset_post_dominators_phase_process(self, all_blocks, **_):
	enter(f"reset_post_dominators_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	if self.target is None or self.target in block.post_dominators:
		post_dominators = set(all_blocks);
	
		if block.post_dominators != post_dominators:
			todo.append(post_dominators_phase(block));
			
			for parent in block.predecessors:
				todo.append(reset_post_dominators_phase(parent, self.target));
			
			block.post_dominators = post_dominators;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















