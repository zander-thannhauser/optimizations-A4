
from debug import *;

from instruction.self import instruction;

from .common import consider;

def optimize_i2f(ins, out, **stuff):
	enter(f"optimize_i2f(ins = {ins})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	valnum = consider(stuff, "i2f", ins = (ivn, ), out = out);
	
	exit("return");
