
from debug import *;

from instruction.self import instruction;

def optimize_iwrite(ops, vrtovn, ins, out, expression_table, label, **_):
	enter(f"optimize_iwrite(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	iwrite = instruction("iwrite", [ivn], None);
	
	ops.append(iwrite);
	
	exit("return");
