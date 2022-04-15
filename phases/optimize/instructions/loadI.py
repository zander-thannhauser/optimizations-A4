
from debug import *;

from expression_table.constant.self import constant;

def optimize_loadI(ops, const, out, expression_table, **_):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	result = expression_table.extovn(constant(value = const));
	
	expression_table.avrwvn(out, result.valnum);
	
	exit("return;");
	return [];


