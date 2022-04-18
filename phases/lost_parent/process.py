
from debug import *;

from phases.lost_parent.self import lost_parent_phase;

def is_reachable(block, start):
	enter(f"is_reachable(block = {block}, start = {start})");
	upward_reachable = None;
	new_upward_reachable = set([block]);
	
	while upward_reachable != new_upward_reachable:
		upward_reachable = new_upward_reachable;
		new_upward_reachable = set.union(new_upward_reachable, \
			*[b.predecessors for b in upward_reachable]);
	
	dprint(f"upward_reachable = {[u.rpo for u in upward_reachable]}")
	
	retval = start in upward_reachable;
	exit(f"return {retval};");
	return retval;

def lost_parent_phase_process(self, start, all_blocks, **_):
	enter(f"lost_parent_phase.process(block.rpo = {self.block.rpo})");
	
	todo = [];
	
	block = self.block;
	
	# should traverse upwards to start, it's unreachable if it
	# reached dead-ends or loops (while-changed)
	
	if block.is_reachable and block != start:
		
		block.is_reachable = is_reachable(block, start);
		
		if not block.is_reachable:
			
			for child in block.successors:
				dprint(f"{str(child)}.predecessors = {[p.po for p in child.predecessors]}");
				child.predecessors.remove(block);
				dprint(f"{str(child)}.predecessors = {[p.po for p in child.predecessors]}");
				todo.append(lost_parent_phase(child));
			
			all_blocks.remove(block);
			
			block.successors = [];
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















