
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

def optimize_mult_vr(ops, vrtovn, avin, et, lvn, rvn, out = None):
	enter(f"optimize_mult_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# a * b => (a * b)
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, vrtovn, avin, et, a * b, out);
		
		# X * 0 or 0 * X => 0
		case (constant(value = 0), _) | (_, constant(value = 0)):
			assert(not "TODO");
		
		# X * 1 => X
		case (_, constant(value = 1)):
			assert(not "TODO");
		
		# 1 * X => X
		case (constant(value = 1), _):
			assert(not "TODO");
		
		# a * (X + b) => a * X + a * b
		case (constant(value = a), expression(op = "addI", ins = (X, ), const = b)):
			subvn = consider(ops, vrtovn, avin, et, "multI", (X, ), const = a);
			valnum = consider(ops, vrtovn, avin, et, "addI", (subvn, ), const = a * b, out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_mult(ops, vrtovn, avin, ins, out, expression_table, **_):
	enter(f"optimize_mult(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_mult_vr(ops, vrtovn, avin, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];






