
from debug import *;

from expression_table.constant.self import constant;
from expression_table.multiplicity.self import multiplicity;
from expression_table.unordered.self import unordered;
from expression_table.expression.self import expression;

from .common import consider_exp, consider_multi, load_literal;

def comp(a, b):
	if a > b:
		return 1;
	elif a < b:
		return -1;
	else:
		return 0;

def optimize_comp_vn(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_comp_vn(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# constant-fold:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(vrtovn, et, comp(a, b), out);
		
		# identities:
		# comp(X, X) = 0
		case (_, _) if lvn == rvn:
			valnum = load_literal(vrtovn, et, 0, out);
		
		# substitutions:
		# (addI X, a) vs b => X vs (b - a)
		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
			# valnum = optimize_comp_vn(ops, et, X, load_literal(ops, et, b - a), out);
			assert(not "TODO");
		
		case (constant(value = b), expression(op = "addI", ins = [X], const = a)):
			assert(not "TODO");
		
		# (addI X, a) vs (addI Y, b) => X vs (addI Y, max(a,b) - min(a, b))
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
				# if d == a or d == b:
					# then it's a good idea: keeps the instruction
					# count the same
				# lsubvn = optimize_mult_vr(load_literal(a // d), X);
				# rsubvn = optimize_mult_vr(load_literal(b // d), X);
				# valnum = optimize_comp_vn(lsubvn, rsubvn);
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		case (multiplicity(op = op_a, ins = A), constant(value = 0)):
			assert(not "TODO");
		
		case (constant(value = 0), multiplicity(op = op_a, ins = A)):
			assert(not "TODO");
		
		case (multiplicity(op = op_a, ins = A),
		      multiplicity(op = op_b, ins = B)) if op_a == op_b:
			if len(A) == 1 and len(B) == 1:
				assert(not "TODO");
			else:
				difference = multiplicity.difference(A, B);
				
				# move positives left, move negatives right
				# if empty: consider as zero
				# if either's length <= 1, call self
				# otherwise: return consider()
				
#				if len(difference) == 1:
#					# compare against zero
#					assert(not "TODO");
#				elif len(difference) == 2:
#					# move one to the other side
#					assert(not "TODO");
#				else:
#					subvalnum = consider_multi(vrtovn, et, op_a, difference);
#					valnum = optimize_comp_vn(vrtovn, et, subvalnum, \
#						load_literal(vrtovn, et, 0), out);
				assert(not "TODO");
		
		case (unordered(op = op_a, ins = A),
		      unordered(op = op_b, ins = B)) if op_a == op_b:
			# subtract intersection
			assert(not "TODO");
		
		# default:
		case (_, _):
			# valnum = consider(ops, et, "comp", (lvn, rvn), out);
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_comp(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_comp(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_comp_vn(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];














