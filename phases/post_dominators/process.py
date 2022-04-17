
from debug import *;

from phases.post_dominators.self import post_dominators_phase;

def post_dominators_phase_process(self, all_blocks, **_):
	enter(f"post_dominators_phase_process(block.po = {self.block.po})");
	
	block = self.block;
	
	dprint(f"len(block.successors) = {len(block.successors)}")
	
	new_post_dominance_frontier = set();
	
	match len(block.successors):
		case 0:
			post_dominators = set();
		case 1:
			child, = block.successors;
			post_dominators = child.post_dominators.copy();
			block.post_immediate_dominator = child;
		case _:
			successors_post_dominators = [p.post_dominators for p in block.successors];
			post_dominators = set.intersection(*successors_post_dominators);
			block.post_immediate_dominator = min(post_dominators, key = lambda b: b.rpo);
			new_post_dominance_frontier = set.symmetric_difference(*successors_post_dominators);
	
	if block.post_dominance_frontier != new_post_dominance_frontier:
		for added in set.difference(new_post_dominance_frontier, block.post_dominance_frontier):
			added.reverse_post_dominance_frontier.add(block);
		for removed in set.difference(block.post_dominance_frontier, new_post_dominance_frontier):
			removed.reverse_post_dominance_frontier.discard(block);
		block.post_dominance_frontier = new_post_dominance_frontier;
	
	post_dominators.add(block)
	
	dprint(f"post_dominators = {[str(d) for d in post_dominators]}")
	dprint(f"post_dominance_frontier = {[str(d) for d in block.post_dominance_frontier]}")
	
	todo = [];
	
	if block.post_dominators != post_dominators:
		for predecessor in block.predecessors:
			todo.append(post_dominators_phase(predecessor));
		block.post_dominators = post_dominators;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















