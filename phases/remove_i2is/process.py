
from debug import *;

from phases.remove_i2is.self import remove_i2is_phase;

def remove_i2is_phase_process(self, phase_counters, **_):
	enter(f"remove_i2is.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	newest_instructions = [];
	
	for inst in block.newer_instructions:
		if inst.op == "i2i" and inst.ins[0] == inst.out:
			pass
		else:
			newest_instructions.append(inst);
	
	block.newest_instructions = newest_instructions;
	block.newest_jump = block.newer_jump;
	
	todo = [];
	
	block.phase_counters["remove_i2is"] = phase_counters["remove_i2is"]
	
	for child in block.successors:
		if child.phase_counters["remove_i2is"] < phase_counters["remove_i2is"]:
			todo.append(remove_i2is_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















