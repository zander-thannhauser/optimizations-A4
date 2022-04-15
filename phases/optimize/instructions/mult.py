
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider, load_literal;

def optimize_mult_vr(ops, et, lvn, rvn, out = None):
	enter(f"optimize_mult_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, et, a * b, out);
			
		# identities:
		# 0 * X = 0
		case (constant(value = 0), _):
			assert(not "TODO");
		# 1 * X = X
		case (constant(value = 1), _):
			# avrwvn(out, rvn);
			assert(not "TODO");
		# -1 * X = -X
		case (constant(value = -1), _):
			# avrwvn(out, rvn);
			assert(not "TODO");
		
		# X * 0 = 0
		case (_, constant(value = 0)):
			assert(not "TODO");
		# X * 1 = X
		case (_, constant(value = 1)):
			assert(not "TODO");
		# X * -1 = -X
		case (_, constant(value = -1)):
			assert(not "TODO");
		
#		# substitutions:
		# (addI X, a) * b => addI (multI X, b), (a * b)
		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
			if a * b:
				subvn = consider(ops, et, "multI", ins = (X, ), const = b);
				valnum = consider(ops, et, "addI", ins = (subvn, ), const = (a * b), out = out);
			else:
				assert(not "TODO");
		
		# a * (addI X, b) => addI (multI X, a), (a * b)
		case (constant(value = a), expression(op = "addI", ins = [X], const = b)):
			assert(not "TODO");
		
		# (multI X, a) * b => multI X, (a * b)
		case (expression(op = "multI", ins = [X], const = a), constant(value = b)):
#			consider(ops, et, "multI", (X, a * b), out);
			assert(not "TODO");
		
		# a * (multI X, b) => multI X, (a * b)
		case (constant(value = a), expression(op = "multI", ins = [X], const = b)):
			assert(not "TODO");
		
		# (multI X, a) * (multI Y, b) => multI (mult X Y), (a * b)
		case (expression(op = "multI", ins = [X], const = a), \
		      expression(op = "multI", ins = [Y], const = b)):
			assert(not "TODO");
		
		# mult X, c => multI X, c:
		case (_, constant(value = c)):
#			consider(ops, et, "multI", (lvn, c), out);
			assert(not "TODO");
		
		# mult c, X => multI X, c:
		case (constant(value = c), _):
#			consider(ops, et, "multI", (rvn, c), out);
			assert(not "TODO");
		
#		# default:
		case (lex, rex):
#			print(f"lex, rex = {lex}, {rex}");
#			consider(ops, et, "mult", (lvn, rvn), out);
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_mult(ops, ins, out, expression_table, **_):
	enter(f"optimize_mult(ins = {ins}, out = {out})");
	
	lvn, rvn = expression_table.vrtovn(ins[0]), expression_table.vrtovn(ins[1])
	
	optimize_mult_vr(ops, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];


