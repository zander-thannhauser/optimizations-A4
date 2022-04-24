
from debug import *;

from phases.critical.self import critical_phase;
from phases.superfical_critical.self import superfical_critical_phase;

def superfical_critical_phase_process(self, phase_counters, **_):
	enter(f"superfical_critical.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	assert(block.new_instructions is not None);
	
	for inst in block.new_instructions:
		match inst.op:
			case "addI" | "add" | "fadd" | "mult" | "fmult" | "mod" \
					| "load" | "fload" | "loadI" | "loadAI" \
					| "comp" | "not" | "or" | "i2i" | "i2f" | "f2i" \
					| "multI"  | "loadAO" | "sub" | "rshiftI"\
					| "cmp_GT" | "cmp_EQ" | "cmp_LT" | "cmp_NE" | "cmp_LE" \
					| "cmp_GE":
				pass;
			
			case "call" | "icall" \
				| "store" | "storeAI" | "storeAO" \
				| "iread" | "iwrite" | "swrite" | "putchar":
				todo.append(critical_phase(inst));
			
			case _:
				dprint(f"inst.op = {inst.op}");
				assert(not "TODO");
	
	if block.new_jump is not None:
		match block.new_jump.op:
			case "ret" | "iret":
				todo.append(critical_phase(block.new_jump));
			case "cbr" | "cbr_GT" | "cbr_GE" | "cbr_LE" | "cbr_EQ" | "cbr_LT" | "cbrne":
				pass;
			case jop:
				dprint(f"jop = {jop}");
				assert(not "TODO");
	
	block.phase_counters["superfical-critical"] = phase_counters["superfical-critical"]
	
	for child in block.successors:
		if child.phase_counters["superfical-critical"] < phase_counters["superfical-critical"]:
			todo.append(superfical_critical_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















