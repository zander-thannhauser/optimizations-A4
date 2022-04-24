
from debug import *;

from instruction.self import instruction;

def optimize_iwrite(ops, vrtovn, ins, label, **_):
	enter(f"optimize_iwrite(ins = {ins})");
	
	ivn = vrtovn[ins[0]];
	
	iwrite = instruction("iwrite", [ivn]);
	
	ops.append(iwrite);
	
	exit("return");
