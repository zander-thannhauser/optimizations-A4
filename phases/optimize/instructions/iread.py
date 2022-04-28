
from debug import *;

from instruction.self import instruction;

def optimize_iread(ops, vrtovn, ins, label, **_):
	enter(f"optimize_iread(ins = {ins})");
	
	ivn = vrtovn[ins[0]];
	
	iread = instruction("iread", [ivn]);
	
	ops.append(iread);
	
	exit("return");
