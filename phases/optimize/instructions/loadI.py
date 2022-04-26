
from debug import *;

from instruction.self import instruction;
from expression_table.label.self import label;

from .common import load_literal;

def optimize_loadI(const, out, **stuff):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	if type(const) is int:
		load_literal(stuff, const, out);
	else:
		exp = label(const);
		
		et = stuff["expression_table"];
		avin = stuff["avin"];
		ops = stuff["ops"];
		vrtovn = stuff["vrtovn"];
		
		result = et.extovn(exp);
		
		if result.valnum not in avin:
			new = instruction("loadI", [], const = const, out = result.valnum);
			dprint(f"new = {new}")
			avin.add(result.valnum);
			ops.append(new);
	
		vrtovn[out] = result.valnum;
		
	exit("return;");
	return [];


