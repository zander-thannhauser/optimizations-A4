
from debug import *;

from phases.loop_depth.self import loop_depth_phase;

def loop_depth_phase_process(self, start, **_):
	enter(f"loop_depth.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	if block == start:
		loop_depth = 0;
		public_loop_depth = 0;
	else:
		loop_depth = max(
			p.public_loop_depth \
			for p in block.predecessors \
			if p.public_loop_depth is not None);
		
		# am I a loop-header?
		if any(block in p.dominators for p in block.predecessors):
			loop_depth += 1;
		
		public_loop_depth = loop_depth;
		
		# am I a loop-footer?
		if any(block in s.post_dominators for s in block.successors):
			public_loop_depth -= 1;
	
	block.loop_depth = loop_depth;
	
	dprint(f"block.loop_depth = {block.loop_depth}");
	dprint(f"block.public_loop_depth = {block.public_loop_depth}");
	
	todo = [];
	
	if block.public_loop_depth != public_loop_depth:
		for child in block.successors:
			todo.append(loop_depth_phase(child));
		block.public_loop_depth = public_loop_depth;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















