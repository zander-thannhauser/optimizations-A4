
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider, load_literal;
from .add import optimize_add_vr;

def optimize_sub_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, et, a - b, out);
		
		# identities:
		# X - 0 = X
		case (_, constant(value = 0)):
			valnum = et.avrwvn(out, lvn);
		
		case (constant(value = 0), _):
			assert(not "TODO");
		
		# X - X = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
#		
		# substitutions:
		# (addI X, a) - b => addI X, (a - b)
		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
			if a - b == 0:
				valnum = et.avrwvn(out, X);
			else:
				valnum = consider(ops, et, "addI", (X, ), out, const = a - b);
		
		# a - (addI X, b) => sub (a - b), X
		case (constant(value = a), expression(op = "addI", ins = [X], const = b)):
			assert(not "TODO");
		
		# (add X, Y) - (add Z, Y) => X - Z
		case (expression(op = "add", ins = [A, B]), \
			  expression(op = "add", ins = [C, D])) if B == D:
			assert(not "TODO");
		
		# (add X, Y) - Y => X
		case (expression(op = "add", ins = [X, Y]), _) if Y == rvn:
			assert(not "TODO");
		
		# (sub X, Y) - X => Y
		# (sub X, Y) - Z => X - (Y + Z)
		case (expression(op = "sub", ins = [X, Y]), _):
			if X == rvn:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# (addI X, a) - (addI Y, b) => addI (sub X, Y), (a - b)
		case (expression(op = "addI", ins = [X], const = a), \
		      expression(op = "addI", ins = [Y], const = b)):
			if X == Y:
				assert(not "TODO");
			elif a - b == 0:
				valnum = optimize_sub_vr(ops, et, X, Y, out);
			else:
#				subvn = optimize_sub_vr(ops, et, X, Y);
#				retval = consider(ops, et, "addI", (subvn, a - b), out);
				assert(not "TODO");
		
		# (multI X, a) - (multI Y, a) = multI (sub X, Y), a
		case (expression(op = "multI", ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)) if a == b:
			# divide both inner multIs by d, create outer multI
			assert(not "TODO");
		
		# (addI X, a) - (multI Y, b) = (Y * -b + X) + a
		case (expression(op = "addI",  ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)):
#			subvn1 = consider(ops, et, "multI", (Y, -b));
#			subvn2 = optimize_add_vr(ops, et, X, subvn1);
#			retval = consider(ops, et, "addI", (subvn2, a), out);
			assert(not "TODO");
		
		# X - (addI Y, a) = (sub X, Y) - a
		case (_, expression(op = "addI", ins = [Y], const = b)):
#			subvn = optimize_sub_vr(ops, et, lvn, Y, out);
#			retval = consider(ops, et, "addI", (subvn, -b), out);
			assert(not "TODO");
		
		# X - (multI Y, a) = X + (multI Y, -a)
		case (_, expression(op = "multI", ins = [Y], const = b)):
			subvn = consider(ops, et, "multI", (Y,), const = -b);
			valnum = optimize_add_vr(ops, et, lvn, subvn, out);
		
		# X - c => addI X, -c
		case (_, constant(value = c)):
			valnum = consider(ops, et, "addI", (lvn,), out, const = -c);
		
		# default:
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			# consider(ops, ("sub", lvn, rvn), out);
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_sub(ops, ins, out, expression_table, **_):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = expression_table.vrtovn(ins[0]), expression_table.vrtovn(ins[1])
	
	optimize_sub_vr(ops, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];


