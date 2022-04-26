
from debug import *;

from instruction.self import instruction;

def optimize_call(ops, vrtovn, ins, label, **_):
	enter(f"optimize_call(ins = {ins})");
	
	ivns = [vrtovn[i] for i in ins];
	
	call = instruction("call", ivns, label = label);
	
	ops.append(call);
	
	exit("return");
