
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
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
		
		# (X + a) vs. b => X vs. (b - a)
		case (expression(op = "addI", ins = (X, ), const = a), constant(value = b)):
			subrvn = load_literal(stuff, b - a);
			valnum = optimize_comp_vn(stuff, X, subrvn, out);
		
		case (expression(op = "addI", ins = (X, ), const = a), phi()):
			if X == lvn:
				assert(not "TODO");
			else:
				valnum = consider(stuff, "comp", (lvn, rvn), out = out);
		
		case (parameter() | phi() | unknown() | expression(op = "f2i"), constant() | unknown()):
			valnum = consider(stuff, "comp", (lvn, rvn), out = out);
		
		case (constant() | unknown(), parameter() | phi() | unknown() | expression(op = "f2i")):
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














