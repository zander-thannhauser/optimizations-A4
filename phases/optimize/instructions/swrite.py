
from debug import *;

from instruction.self import instruction;

def optimize_swrite(ops, vrtovn, ins, label, **_):
	enter(f"optimize_swrite(ins = {ins})");
	
	ivn = vrtovn[ins[0]];
	
	swrite = instruction("swrite", [ivn]);
	
	ops.append(swrite);
	
	exit("return");
