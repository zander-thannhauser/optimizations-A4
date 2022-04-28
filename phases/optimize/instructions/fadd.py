
from debug import *;

from instruction.self import instruction;

from .common import consider;

def optimize_fadd(ins, out, **stuff):
	enter(f"optimize_fadd(ins = {ins})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]];
	
	valnum = consider(stuff, "fadd", (min(lvn, rvn), max(lvn, rvn)), out = out);
	
	exit("return");
