
from debug import *;

from phases.syntax_lookup.self import syntax_lookup_phase;

def syntax_lookup_phase_process(self, syntax_lookup, usage, phase_counters, **_):
	enter(f"syntax_lookup_phase_process(block.rpo = {self.block.rpo})");
	
	todo = [];
	
	block = self.block;
	
	for inst in block.original_instructions:
		match inst.op:
			# expression: 0 ins, 1 out:
			case "loadI":
				out = inst.out;
				syntax_lookup[out] = inst;
			
			# expression: 1 ins, 1 out:
			case "testgt" | "testlt" | "testle" | "testge" | "testeq" | "testne" | "load" | "i2f" | "f2i" | "fload":
				i, = inst.ins;
				out = inst.out;
				usage.setdefault(i, set()).add(out);
				syntax_lookup[out] = inst;
			
			# expression: 2 ins, 1 out:
			case "add" | "fadd" | "sub" | "mult" | "fmult" | "comp" | "mod" | "or" | "rshift":
				l, r = inst.ins;
				out = inst.out;
				usage.setdefault(l, set()).add(out);
				usage.setdefault(r, set()).add(out);
				syntax_lookup[out] = inst;
			
			# non-expressions or unmoveables:
			case "i2i" | "store" | "iwrite" | "call" | "swrite" | "iread" | "icall" | "putchar":
				pass
			
			case _:
				dprint(f"inst.op = {inst.op}")
				assert(not "TODO");
	
	block.phase_counters["syntax-lookup"] = phase_counters["syntax-lookup"]
	
	for child in block.successors:
		if child.phase_counters["syntax-lookup"] < phase_counters["syntax-lookup"]:
			todo.append(syntax_lookup_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















