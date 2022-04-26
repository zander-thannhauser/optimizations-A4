
from debug import *;

from expression_table.phi.self import phi;
from expression_table.parameter.self import parameter;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

#from .mult import optimize_mult_vr;

def optimize_add_vr(stuff, lvn, rvn, out = None):
	enter(f"optimize_add_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	vrtovn = stuff["vrtovn"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(stuff, literal = a + b, out = out);
		
		case (_, constant(value = 0)):
			if out is not None: vrtovn[out] = lvn;
			valnum = lvn;
		
		case (constant(value = 0), _):
#			if out is not None: vrtovn[out] = rvn;
#			valnum = rvn;
			assert(not "TODO");
		
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# a * X + b * X => (a + b) * X
		case (expression(op = "multI", ins = (X, ), const = a), \
		      expression(op = "multI", ins = (Y, ), const = b)) if X == Y:
			assert(not "TODO");
		
		# a * X + a * Y => a * (X + Y)
		case (expression(op = "multI", ins = (X, ), const = a), \
		      expression(op = "multI", ins = (Y, ), const = b)) if a == b:
			assert(not "TODO");
		
		# a * X + X => (a + 1) * X
		case (expression(op = "multI", ins = (X, ), const = a), _) if X == rvn:
			match a + 1:
				case 0: assert(not "TODO");
				case 1: assert(not "TODO");
				case _:
#					valnum = consider(ops, vrtovn, avin, et, \
#						"multI", (X, ), const = a + 1, out = out);
					assert(not "TODO");
		
		# X + a * X => (a + 1) * X
		case (_, expression(op = "multI", ins = (X, ), const = a)) if lvn == X:
			assert(not "TODO");
		
		case (expression(op = "multI"), constant(value = a)):
			valnum = consider(stuff, "addI", ins = (lvn, ), const = a, out = out);
		
		case (phi() | parameter(), constant(value = a)):
			valnum = consider(stuff, "addI", ins = (lvn, ), const = a, out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_add(ins, out, **stuff):
	enter(f"optimize_add(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_add_vr(stuff, lvn, rvn, out);
	
	exit("return;");
	return [];






















