
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

from .add import optimize_add_vr;
from .mult import optimize_mult_vr;

def optimize_sub_vr(ops, vrtovn, avin, et, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
			
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, vrtovn, avin, et, literal = a - b, out = out);
		
		case (_, constant(value = 0)):
			assert(not "TODO");
		
		# (X + a) - (Y + b) => (X - Y) + (a - b)
		case (expression(op = "addI", ins = (X, ), const = a), \
		      expression(op = "addI", ins = (Y, ), const = b)):
			assert(not "TODO");
		
		# (X + a) - Y => (X - Y) + a
		case (expression(op = "addI", ins = (X, ), const = a), _):
			subvn = optimize_sub_vr(ops, vrtovn, avin, et, X, rvn);
			valnum = consider(ops, vrtovn, avin, et, "addI", (subvn, ), const = a, out = out);
		
		# a * X - b * X => (a - b) * X
		case (expression(op = "multI", ins = (X, ), const = a), \
		      expression(op = "multI", ins = (Y, ), const = b)) if X == Y:
			assert(not "TODO");
		
		# a * X - a * Y => a * (X - Y)
		case (expression(op = "multI", ins = (X, ), const = a), \
		      expression(op = "multI", ins = (Y, ), const = b)) if a == b:
			assert(not "TODO");
		
		# a * X + X => (a - 1) * X
		case (expression(op = "multI", ins = (X, ), const = a), _) if X == rvn:
			match a - 1:
				case 0: assert(not "TODO");
				case 1:
					if out is not None: vrtovn[out] = X
					valnum = X;
				case _: assert(not "TODO");
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_sub(ops, vrtovn, avin, ins, out, expression_table, **_):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_sub_vr(ops, vrtovn, avin, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];












