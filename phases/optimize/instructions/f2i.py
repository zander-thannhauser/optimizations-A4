
from debug import *;

from instruction.self import instruction;

from .common import consider;

def optimize_f2i(ins, out, **stuff):
	enter(f"optimize_f2i(ins = {ins})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	valnum = consider(stuff, "f2i", ins = (ivn, ), out = out);
	
	exit("return");
