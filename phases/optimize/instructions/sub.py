
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from .common import consider_multi;

from .add import optimize_add_vr;
from .mult import optimize_mult_vr;

def optimize_sub_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(ops, et, a - b, out);
		
		# identities:
		# X - 0 = X
		case (_, constant(value = 0)):
			valnum = et.avrwvn(out, lvn);
		
		# 0 - X = -X
		case (constant(value = 0), _):
			assert(not "TODO");
		
		# X - X = 0
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# substitutions:
		# (addI X, a) - (addI X, b) => (a - b)
		# (addI X, a) - (addI Y, a) => sub X, Y
		# (addI X, a) - (addI Y, b) => addI (sub X, Y), (a - b)
		case (expression(op = "addI", ins = [X], const = a), \
		      expression(op = "addI", ins = [Y], const = b)):
			if X == Y:
				assert(not "TODO");
			elif a - b == 0:
				# valnum = optimize_sub_vr(ops, et, X, Y, out);
				assert(not "TODO");
			else:
#				subvn = optimize_sub_vr(ops, et, X, Y);
#				retval = consider(ops, et, "addI", (subvn, a - b), out);
				assert(not "TODO");
		
		# sum(A) - sum(B) => sum(A - B)
		case (multiplicity(op = "sum", ins = A), \
			  multiplicity(op = "sum", ins = B)):
			difference = multiplicity.difference(A, B);
			if len(difference) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", difference, out);
		
		# (multI X, a) - (multI X, b) = multI X, (a - b)
		# (multI X, a) - (multI Y, a) = multI (sub X, Y), a
		# (multI X, a) - (multI Y, b) = multiplicity(a * [X] - b * [Y])
		case (expression(op = "multI", ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)):
#			if a == b:
#				# divide both inner multIs by d, create outer multI
#				assert(not "TODO");
			assert(not "TODO");
		
		# product(A) - product(B) => product(A <I> B) * (product(A - B) - product(B - A))
		case (multiplicity(op = "product", ins = A), \
			  multiplicity(op = "product", ins = B)):
			# subtract the intersection
			intersection = multiplicity.intersection(A, B);
			
			if len(intersection):
				AB = multiplicity.difference(A, intersection);
				BA = multiplicity.difference(B, intersection);
				
				if len(AB) == 0:
					lvn = load_literal(vrtovn, et, 1);
				elif len(AB) == 1 and AB[0][1] == 1:
					lvn = AB[0][0];
				else:
					lvn = consider_multi(vrtovn, et, "product", AB);
				
				if len(BA) == 0:
					rvn = load_literal(vrtovn, et, 1);
				elif len(BA) == 1 and BA[0][1] == 1:
					rvn = BA[0][0];
				else:
					rvn = consider_multi(vrtovn, et, "product", BA);
				
				lvn = optimize_sub_vr(vrtovn, et, lvn, rvn);
				
				rvn = consider_multi(vrtovn, et, "product", intersection);
				
				valnum = optimize_mult_vr(vrtovn, et, lvn, rvn, out);
			else:
				assert(not "TODO");
		
		# ∑(X) - (multI, Y, a) = ∑(X - a * [Y]):
		case (multiplicity(op = "sum", ins = X), \
			  expression(op = "multI", ins = [Y], const = b)):
			assert(not "TODO");
		
		# (multI, X, a) - ∑(Y) = ∑(a * [X] - Y):
		case (expression(op = "multI", ins = [Y], const = b), \
		      multiplicity(op = "sum", ins = X)):
			assert(not "TODO");
		
		# (addI X, a) - (multI Y, b) = (Y * -b + X) + a
		case (expression(op = "addI",  ins = [X], const = a), \
			  expression(op = "multI", ins = [Y], const = b)):
#			subvn1 = consider(ops, et, "multI", (Y, -b));
#			subvn2 = optimize_add_vr(ops, et, X, subvn1);
#			retval = consider(ops, et, "addI", (subvn2, a), out);
			assert(not "TODO");
		
		# X - (multI Y, a) = X + (multI Y, -a)
		case (_, expression(op = "multI", ins = [Y], const = b)):
			# subvn = consider(ops, et, "multI", (Y,), const = -b);
			# valnum = optimize_add_vr(ops, et, lvn, subvn, out);
			assert(not "TODO");
		
		# (sub X, Y) - X => Y
		# (sub X, Y) - Z => X - (Y + Z)
		case (expression(op = "sub", ins = [X, Y]), _):
			if X == rvn:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# X - c => addI X, -c
		case (_, constant(value = c)):
			# valnum = consider(ops, et, "addI", (lvn,), out, const = -c);
			assert(not "TODO");
		
		# sum(A) - B => sum(A - [B])
		case (multiplicity(op = "sum", ins = A), _):
			difference = multiplicity.difference(A, [(rvn, 1)]);
			if len(difference) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", difference, out);
		
		# default:
		case (lex, rex):
			valnum = consider_multi(vrtovn, et, "sum", sorted([(lvn, 1), (rvn, -1)]), out);
	
	exit(f"return {valnum};");
	return valnum;

def optimize_sub(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_sub_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];












