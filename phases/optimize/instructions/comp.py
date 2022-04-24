
from debug import *;

from expression_table.constant.self import constant;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from .common import consider, load_literal;

def comp(a, b):
	if a > b:
		return 1;
	elif a < b:
		return -1;
	else:
		return 0;

def optimize_comp_vn(stuff, lvn, rvn, out = None):
	enter(f"optimize_comp_vn(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(stuff, comp(a, b), out);
		
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		case (parameter(), constant()):
			valnum = consider(stuff, "comp", (lvn, rvn), out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_comp(ins, out, **stuff):
	enter(f"optimize_comp(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_comp_vn(stuff, lvn, rvn, out);
	
	exit("return;");
	return [];














