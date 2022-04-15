
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider, load_literal;

def comp(a, b):
	if a > b:
		return 1;
	elif a < b:
		return -1;
	else:
		return 0;

def optimize_comp_vn(ops, et, lvn, rvn, out = None):
	enter(f"optimize_comp_vn(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-fold:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, et, comp(a, b), out);
		
		# identities:
		# comp(X, X) = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) vs b => X vs (b - a)
		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
			valnum = optimize_comp_vn(ops, et, X, load_literal(ops, et, b - a), out);
		
		case (constant(value = b), expression(op = "addI", ins = [X], const = a)):
			assert(not "TODO");
		
		# (addI X, a) vs (addI Y, b) => X vs (addI Y, b - a)
		case (expression(op = "addI", ins = [X], const = a), \
			  expression(op = "addI", ins = [Y], const = b)):
#			if X == Y:
#				assert(not "TODO");
#			elif a == b:
#				# after you've canceled the adds on both sides,
#				# is the inner expression a multiply?
#				# if so: try to cancel those factors
#				assert(not "TODO");
#			else:
#				# or whichever's lower
#				assert(not "TODO");
			assert(not "TODO");
		
		case (expression(op = "add", ins = [A, B]), \
		      expression(op = "add", ins = [C, D])):
			if A == C:
				assert(not "TODO");
			elif B == D:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		case (expression(op = "sub", ins = [X, Y]), constant(value = c)):
			# if Y is an addI, then you can bring it across
			assert(not "TODO");
		
		case (expression(op = "sub", ins = [X, Y]), constant(value = 0)):
			assert(not "TODO");
		
		case (constant(value = 0), expression(op = "sub", ins = [X], const = a)):
			assert(not "TODO");
		
		case (constant(value = c), expression(op = "sub", ins = [X], const = a)):
			assert(not "TODO");
		
		case (expression(op = "sub", ins = [A, B]),
		      expression(op = "sub", ins = [C, D])):
			if A == C:
				assert(not "TODO");
			elif B == D:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		case (expression(op = "multI", ins = [X], const = a), constant(value = b)):
			assert(not "TODO");
		
		case (constant(value = b), expression(op = "multI", ins = [X], const = a)):
			assert(not "TODO");
			
		# (multI X, a) vs (multI X, b) => a vs b
		case (expression(op = "multI", ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)):
			if X == Y:
				assert(not "TODO");
			elif (d := gcd(a, b)) != 1:
				# lsubvn = optimize_mult_vr(load_literal(a // d), X);
				# rsubvn = optimize_mult_vr(load_literal(b // d), X);
				# valnum = optimize_comp_vn(lsubvn, rsubvn);
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		case (expression(op = "mult", ins = [A, B]),
		      expression(op = "mult", ins = [C, D])):
#			if A == C:
#				assert(not "TODO");
#			elif B == D:
#				assert(not "TODO");
#			else:
#				assert(not "TODO");
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			dprint(f"lex, rex = {lex}, {rex}");
			valnum = consider(ops, et, "comp", (lvn, rvn), out);
	
	exit(f"return {valnum};");
	return valnum;

def optimize_comp(ops, ins, out, expression_table, **_):
	enter(f"optimize_comp(ins = {ins}, out = {out})");
	
	lvn, rvn = expression_table.vrtovn(ins[0]), expression_table.vrtovn(ins[1])
	
	optimize_comp_vn(ops, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];














