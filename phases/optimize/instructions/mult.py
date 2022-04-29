
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

def optimize_mult_vr(stuff, lvn, rvn, out = None):
	enter(f"optimize_mult_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# a * b => (a * b)
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(stuff, a * b, out);
		
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
			subvn = consider(stuff, "multI", (X, ), const = a);
			valnum = consider(stuff, "addI", (subvn, ), const = a * b, out = out);
		
		# (X + a) * b => b * X + a * b
		case (expression(op = "addI", ins = (X, ), const = a), constant(value = b)):
			subvn = consider(stuff, "multI", (X, ), const = b);
			valnum = consider(stuff, "addI", (subvn, ), const = a * b, out = out);
		
		# (X * a) * b => X * (a * b)
		case (expression(op = "multI", ins = (X, ), const = a), constant(value = b)):
			valnum = consider(stuff, "multI", (X, ), const = a * b, out = out);
		
		# (a * X) * Y => a * (X * Y)
		case (expression(op = "multI", ins = (X, ), const = a), phi()):
			subvn = optimize_mult_vr(stuff, X, rvn);
			valnum = consider(stuff, "multI", (subvn, ), const = a, out = out);
			assert(not "CHECK");
		
		# c * X => (c * X)
		case (constant(value = a), phi()):
			valnum = consider(stuff, "multI", (rvn, ), const = a, out = out);
		
		# X * c => (c * X)
		case (phi() | unknown() | parameter(), constant(value = a)):
			valnum = consider(stuff, "multI", (lvn, ), const = a, out = out);
		
		case (unknown(), phi()):
			valnum = consider(stuff, "mult", (min(lvn, rvn), max(lvn, rvn)), out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_mult(ins, out, **stuff):
	enter(f"optimize_mult(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_mult_vr(stuff, lvn, rvn, out);
	
	exit("return;");
	return [];






