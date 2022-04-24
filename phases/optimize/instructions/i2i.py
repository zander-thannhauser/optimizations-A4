
from debug import *;

def optimize_i2i(vrtovn, ins, out, **_):
	enter(f"optimize_i2i(ins = {ins}, out = {out})");
	
	vrtovn[out] = vrtovn[ins[0]];
	
	exit("return;");
	return [];


