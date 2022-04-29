
from debug import *;

from instruction.self import instruction;

from expression_table.unknown.self import unknown;

def optimize_icall(ops, vrtovn, expression_table, avin, ins, out, label, **_):
	enter(f"optimize_call(ins = {ins})");
	
	ivns = [vrtovn[i] for i in ins];
	
	icallex = unknown(id);
	oresult = expression_table.extovn(icallex);
	ovn = oresult.valnum;
	
	icall = instruction("icall", ivns, label = label, out = ovn);
	
	icallex.instruction = icall;
	ops.append(icall);
	
	vrtovn[out] = ovn;
	avin.add(ovn);
	
	exit("return");
