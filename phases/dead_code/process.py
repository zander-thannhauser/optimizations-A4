
from debug import *;

from phases.lost_parent.self import lost_parent_phase;
from phases.dead_code.self import dead_code_phase;

def dead_code_phase_process(self, start, all_blocks, phase_counters, **_):
	enter(f"dead_code_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	new_instructions = [];
	
	for inst in block.new_instructions:
		if inst.is_critical:
			new_instructions.append(inst);
	
	if block.new_jump is not None and not block.new_jump.is_critical:
#		# who are my children?
#		for child in block.successors:
#			child.predecessors.remove(block);
#			todo.append(lost_parent_phase(child));
#		child = block.post_immediate_dominator;
#		child.predecessors.append(block);
#		block.successors = [child];
#		block.jump = None;
		assert(not "TODO");
	
	if len(new_instructions) == 0 and block.new_jump is None and block != start:
		dprint(f"block.rpo = {block.rpo}");
		dprint(f"block.label = {block.label}");
		child, = block.successors;
		
		dprint(f"child = {child}");
		
		assert(block.predecessors);
		
		for parent in block.predecessors:
			if parent.new_jump and parent.new_jump.label == block.label:
				if not child.label:
					assert(not "TODO");
				parent.new_jump.label = child.label;
				parent.successors[1] = child;
			else:
				parent.successors[0] = child;
			dprint(f"{str(parent)}.successors = {[s.po for s in parent.successors]}")
		
		child.predecessors += block.predecessors;
		block.predecessors = [];
		todo.append(lost_parent_phase(block));
	
	block.new_instructions = new_instructions;
	
	block.phase_counters["dead-code"] = phase_counters["dead-code"];
	
	for child in block.successors:
		if child.phase_counters["dead-code"] < phase_counters["dead-code"]:
			todo.append(dead_code_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















