
from debug import *;

from instruction.self import instruction;

from phases.critical.self import critical_phase;

def optimize_iwrite(ops, ins, out, expression_table, todo, label, **_):
	enter(f"optimize_iwrite(ins = {ins}, out = {out})");
	
	ivn = expression_table.vrtovn(ins[0]);
	
	iwrite = instruction("iwrite", [ivn], None);
	
	iwrite.is_critical = True;
	todo.append(critical_phase(iwrite));
	
	ops.append(iwrite);
	
	exit("return");
