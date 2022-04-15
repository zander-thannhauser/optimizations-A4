
from debug import *;

from phases.lost_parent.self import lost_parent_phase;

def lost_parent_phase_process(self, all_blocks, **_):
	enter(f"lost_parent_phase.process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	if block.is_reachable and len(block.predecessors) == 0:
		
		for child in block.successors:
			dprint(f"{str(child)}.predecessors = {[p.po for p in child.predecessors]}");
			child.predecessors.remove(block);
			dprint(f"{str(child)}.predecessors = {[p.po for p in child.predecessors]}");
			todo.append(lost_parent_phase(child));
		
		all_blocks.remove(block);
		
		block.successors = [];
		self.is_reachable = False;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;












