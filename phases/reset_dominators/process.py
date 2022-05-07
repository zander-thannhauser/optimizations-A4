
from debug import *;

from phases.reset_dominators.self import reset_dominators_phase;
from phases.dominators.self import dominators_phase;

def reset_dominators_phase_process(self, all_blocks, **_):
	enter(f"reset_dominators_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	if self.target is None or self.target in block.dominators:
		dominators = set(all_blocks);
		
		if block.dominators != dominators:
			todo.append(dominators_phase(block));
			
			for child in block.successors:
				todo.append(reset_dominators_phase(child, self.target));
				
			block.dominators = dominators;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















