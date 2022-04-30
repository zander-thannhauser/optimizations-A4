
from debug import *;

from expression_table.phi.self import phi;
from expression_table.constant.self import constant;
from expression_table.unknown.self import unknown;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

from .add import optimize_add_vr;
from .mult import optimize_mult_vr;

def optimize_sub_vr(stuff, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	
	vrtovn = stuff["vrtovn"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
			
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(stuff, literal = a - b, out = out);
		
		case (_, constant(value = 0)):
			if out is not None: vrtovn[out] = lvn;
			valnum = lvn;
		
		case (constant(value = 0), _):
			valnum = consider(stuff, "multI", (rvn, ), const = -1, out = out);
		
		case (_, _) if lvn == rvn:
			valnum = load_literal(stuff, literal = 0, out = out);
		
		# (X + a) - (Y + b) => (X - Y) + (a - b)
		case (expression(op = "addI", ins = (X, ), const = a), \
		      expression(op = "addI", ins = (Y, ), const = b)):
			if a - b == 0:
				valnum = optimize_sub_vr(stuff, X, Y, out);
			else:
				subvn = optimize_sub_vr(stuff, X, Y);
				valnum = consider(stuff, "addI", (subvn, ), const = a - b, out = out);
		
		# (X + a) - a => X
		# (X + a) - b => X + (a - b)
		case (expression(op = "addI", ins = (X, ), const = a), constant(value = b)):
			if a - b == 0:
				if out is not None: vrtovn[out] = X;
				valnum = X;
			else:
				valnum = consider(stuff, "addI", (X, ), const = a - b, out = out);
		
		# (X + a) - Y => (X - Y) + a
		case (expression(op = "addI", ins = (X, ), const = a), _):
			subvn = optimize_sub_vr(stuff, X, rvn);
			valnum = consider(stuff, "addI", (subvn, ), const = a, out = out);
		
		# X - (Y + a) => (X - Y) - a
		case (_, expression(op = "addI", ins = (Y, ), const = a)):
			subvn = optimize_sub_vr(stuff, lvn, Y);
			valnum = consider(stuff, "addI", (subvn, ), const = -a, out = out);
		
		# (X + Y) - a * X => (1 - b) * X + Y
		# (X + Y) - a * Y => X + (1 - b) * Y
		case (expression(op = "add", ins = (X, Y), const = a), \
		      expression(op = "multI", ins = (Z, ), const = b)) if Z in (X, Y):
			assert(not "TODO");
		
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
		
		# X - a * X => (1 - a) * X
		case (_, expression(op = "multI", ins = (X, ), const = a)) if lvn == X:
			assert(not "TODO");
		
		# X - a * Y => X + (-a) * Y
		case (_, expression(op = "multI", ins = (Y, ), const = a)) if lvn != Y:
			subrvn = consider(stuff, "multI", ins = (Y, ), const = -a);
			valnum = consider(stuff, "add", ins = (lvn, subrvn), out = out);
		
		# X - c => (X + -c)
		case (phi() | parameter() | unknown(), constant(value = a)):
			valnum = consider(stuff, "addI", ins = (lvn, ), const = -a, out = out);
		
		case (expression(op = "add" | "mod"), constant(value = a)):
			valnum = consider(stuff, "addI", ins = (lvn, ), const = -a, out = out);
		
		case (parameter() | expression(op = "add"), expression(op = "mult")):
			valnum = consider(stuff, "sub", ins = (lvn, rvn), out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_sub(ins, out, **stuff):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_sub_vr(stuff, lvn, rvn, out);
	
	exit("return;");
	return [];












