
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider;

def optimize_add_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_add_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
#			retval = load_literal(ops, et, a + b, out);
			assert(not "TODO");
		
		# identities:
		# 0 + X = X
		case (constant(value = 0), _):
			assert(not "TODO");
		
		# X + 0 = X
		case (_, constant(value = 0)):
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) + b => addI X, (a + b)
		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
#			if a + b == 0:
#				assert(not "TODO");
#			else:
#				retval = consider(ops, et, "addI", (X, a + b), out);
			assert(not "TODO");
		
		# a + (addI X, b) => addI X, (a + b)
		case (constant(value = a), expression(op = "addI", ins = [X], const = b)):
			assert(not "TODO");
		
#		# (sub X, Y) + Y => X
#		# (sub X, Y) + Z => (X + Z) - Y
		case (expression(op = "sub", ins = [X, Y]), _):
			if Y == rvn:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# X + (sub Y, X) => Y
		# X + (sub Y, Z) => (X + Y) - Z
		case (_, expression(op = "sub", ins = [Y, Z])):
			if lvn == Z:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
		case (expression(op = "addI", ins = [X], const = a), \
			  expression(op = "addI", ins = [Y], const = b)):
#			if a + b == 0:
#				assert(not "TODO");
#			else:
#				subvn = optimize_add_vr(ops, et, X, Y);
#				retval = consider(ops, et, "addI", (subvn, a + b), out);
			assert(not "TODO");
		
		# (multI X, a) + (multI, Y, a) => multI (add X, Y), a
		case (expression(op = "multI", ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)):
			assert(not "TODO");
		
		# (addI X, a) + Y => addI (add X, Y), a
		case (expression(op = "addI", ins = [X], const = a), _):
#			subvn = optimize_add_vr(ops, et, X, rvn);
#			retval = consider(ops, et, "addI", (subvn, a), out);
			assert(not "TODO");
		
		# X + (addI Y, a) => addI (add X, Y), a
		case (_, expression(op = "addI", ins = [Y], const = a)):
#			subvn = optimize_add_vr(ops, et, lvn, Y);
#			retval = consider(ops, et, "addI", (subvn, a), out);
			assert(not "TODO");
		
		# (multI X, a) + (multI Y, a) = multI (add X, Y), a
		case (expression(op = "multI", ins = [X], const = a), \
			 (expression(op = "multI", ins = [Y], const = b))) \
			if a == b:
#				# check for using a move instruction's result
#				assert(not "TODO");
			assert(not "TODO");
		
		# X + c => addI X, c
		case (_, constant(value = c)):
			valnum = consider(ops, et, "addI", (lvn,), out, const = c);
		
		# c + X => addI X, c
		case (constant(value = c), _):
#			retval = consider(ops, et, "addI", (rvn, c), out);
			assert(not "TODO");
		
		# default:
		case (_, _):
			valnum = consider(ops, et, "add", (lvn, rvn), out);
	
	exit(f"return {valnum};");
	return valnum;

def optimize_add(ops, ins, out, expression_table, **_):
	enter(f"optimize_add(ins = {ins}, out = {out})");
	
	lvn, rvn = expression_table.vrtovn(ins[0]), expression_table.vrtovn(ins[1])
	
	optimize_add_vr(ops, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];


