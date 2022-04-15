
from debug import *;

def optimize_i2i(ops, ins, out, expression_table, **_):
	enter(f"optimize_i2i(ins = {ins}, out = {out})");
	
	valnum = expression_table.vrtovn(ins[0]);
	
	expression_table.avrwvn(out, valnum);
	
	exit("return;");
	return [];


