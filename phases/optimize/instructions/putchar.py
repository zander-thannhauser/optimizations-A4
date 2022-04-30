
from debug import *;

from instruction.self import instruction;

def optimize_putchar(ops, vrtovn, ins, label, **_):
	enter(f"optimize_putchar(ins = {ins})");
	
	ivn = vrtovn[ins[0]];
	
	putchar = instruction("putchar", [ivn]);
	
	ops.append(putchar);
	
	exit("return");
