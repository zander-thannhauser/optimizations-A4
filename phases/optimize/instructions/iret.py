
from debug import *;

from instruction.self import instruction;

def optimize_iret(ops, vrtovn, ins, label, **_):
	enter(f"optimize_iret(ins = {ins})");
	
	ivn = vrtovn[ins[0]];
	
	iret = instruction("iret", [ivn]);
	
	ops.append(iret);
	
	exit("return");
