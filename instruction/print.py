
from debug import *;

def instruction_print(self, p):
	
	match self.op:
		
		# loadI:
		case "loadI":
			p.printf("%s %s => %s", self.op, self.const, self.out);
		
		# 0 in, 0 out:
		case "ret":
			p.printf("%s", self.op);
			
		# 1 in, 0 out:
		case "iwrite" | "swrite" | "iread" | "iret" | "putchar":
			p.printf("%s %s", self.op, self.ins[0]);
			
		# 1 in, 1 out:
		case "i2i" | "i2f" | "f2i" \
			| "testne" | "testge" | "testgt" | "testlt" | "testle" | "testeq" \
			| "load" | "fload":
			p.printf("%s %s -> %s", self.op, self.ins[0], self.out);
		
		# 1 in, 1 constant, 1 out
		case "addI" | "multI" | "loadAI":
			p.printf("%s %s, %s -> %s", self.op, self.ins[0], self.const, self.out);
		
		# 2 ins, 1 out:
		case "comp" | "add" | "fadd" | "sub" | "mult" | "fmult" | "mod" | "or" | "rshift" | "loadAO" | "cmp_LE":
			p.printf("%s %s, %s => %s", self.op, *self.ins, self.out);
		
		# stores:
		case "store":
			p.printf("store %s => %s", *self.ins);
		
		case "storeAI":
			p.printf("storeAI %s => %s, %s", *self.ins, self.const);
		
		case "storeAO":
			p.printf("storeAO %s => %s, %s", *self.ins);
		
#		# calls:
#		case "call":
#			p.printf("%s %s%s", self.op, self.label, "".join(f", {e}" for e in self.ins));
#		
#		case "icall":
#			p.printf("%s %s%s => %s", self.op, self.label, "".join(f", {e}" for e in self.ins), self.out);
#		
		# jumps:
		case "cbr" | "cbrne":
			p.printf("%s %s -> %s", self.op, self.ins[0], self.label);
		
		case "cbr_GT" | "cbr_GE":
			p.printf("%s %s, %s -> %s", self.op, *self.ins, self.label);
		
		case _:
			dprint(f"self.op == {self.op}");
			assert(not "TODO");













