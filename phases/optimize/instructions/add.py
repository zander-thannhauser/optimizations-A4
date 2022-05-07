
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from .common import consider_multi;
from .common import consider_exp;
from .common import load_literal;

from .mult import optimize_mult_vr;

def optimize_add_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_add_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(vrtovn, et, a + b, out);
		
		# identities:
		# 0 + X = X
		case (constant(value = 0), _):
			assert(not "TODO");
		
		# X + 0 = X
		case (_, constant(value = 0)):
			assert(not "TODO");
		
		# X + X = 2 * X:
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		# (X + a) + Y => (X + Y) + a:
		case (expression(op = "addI", ins = (X, ), const = a), phi()):
			subvn = optimize_add_vr(vrtovn, et, X, rvn);
			valnum = consider_exp(vrtovn, et, "addI", (subvn, ), const = a, out = out);
		
		# (X + a) + (Y + b) => (X + Y) + (a + b):
		case (expression(op = "addI", ins = (X, ), const = a),
		      expression(op = "addI", ins = (Y, ), const = b)):
			if a + b == 0:
				assert(not "TODO");
			else:
				subvn = optimize_add_vr(vrtovn, et, X, Y);
				valnum = consider_exp(vrtovn, et, "addI", (subvn, ), const = a + b, out = out);
		
		# (multI, X, a) + X = multI X, (a + 1)
		# (multI, X, a) + Y = sum(a * [Y] <U> [X])
		case (expression(op = "multI", ins = (X, ), const = a), phi() | parameter()):
			new = multiplicity.union([(rvn, 1)], [(X, a)]);
			if len(new) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", new, out);
		
		# X + (multI, X, a) = multI X, (a + 1)
		# X + (multI, Y, a) = sum([X] <U> a * [Y])
		case (parameter(), expression(op = "multI", ins = (Y, ), const = a)):
			new = multiplicity.union([(lvn, 1)], [(Y, a)]);
			if len(new) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", new, out);
		
		# (X * a) + (Y + b) => (X * a + Y) + a:
		case (expression(op = "multI", ins = (X, ), const = a),
		      expression(op = "addI",  ins = (Y, ), const = b)):
			subvn = optimize_add_vr(vrtovn, et, lvn, Y);
			valnum = consider_exp(vrtovn, et, "addI", (subvn,), const = b, out = out);
		
		case (multiplicity(op = "sum", ins = ins), phi()):
			new = multiplicity.union(ins, [(rvn, 1)]);
			if len(new) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", new, out);
		
		# X + a:
		case (expression(op = "multI") | parameter() | phi() | unknown(), constant(value = a)):
			valnum = consider_exp(vrtovn, et, "addI", (lvn, ), const = a, out = out);
		
		# a + Y:
		case (constant(value = a), phi()):
			valnum = consider_exp(vrtovn, et, "addI", (rvn, ), const = a, out = out);
		
		case (phi(), phi()):
			valnum = consider_multi(vrtovn, et, "sum", sorted([(lvn, 1), (rvn, 1)]), out = out);
		
		# default:
		case (_, _):
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_add(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_add(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_add_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];







##		# substitutions:
#		# (addI X, a) + b => addI X, (a + b)
#		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
##			if a + b == 0:
##				assert(not "TODO");
##			else:
##				retval = consider(ops, et, "addI", (X, a + b), out);
#			assert(not "TODO");
#		
#		# a + (addI X, b) => addI X, (a + b)
#		case (constant(value = a), expression(op = "addI", ins = [X], const = b)):
#			assert(not "TODO");
#		
#		# (addI X, a) + (addI, Y, b) => addI (add X, Y), (a + b)
#		case (expression(op = "addI", ins = [X], const = a), \
#			  expression(op = "addI", ins = [Y], const = b)):
##			if a + b == 0:
##				assert(not "TODO");
##			else:
##				subvn = optimize_add_vr(ops, et, X, Y);
##				retval = consider(ops, et, "addI", (subvn, a + b), out);
#			assert(not "TODO");
#		
##		# (addI X, a) + Y => addI (add X, Y), a
#		
##		# X + (addI Y, a) => addI (add X, Y), a
#		
#		# ∑(X) + ∑(Y) => ∑(X + Y):
#		case (multiplicity(op = "sum"), multiplicity(op = "sum")):
#			assert(not "TODO");
#		
#		# (multI, X, a) + ∑(Y) = ∑(a * [X] + Y):
#		case (expression(op = "multI", ins = [Y], const = b), \
#		      multiplicity(op = "sum", ins = X)):
#			assert(not "TODO");
#		
#		# ∑(X) + (multI, Y, a) = ∑(X + a * [Y]):
#		case (multiplicity(op = "sum", ins = X), \
#			  expression(op = "multI", ins = [Y], const = b)):
#			assert(not "TODO");
#		
#		# (multI X, a) + (multI, Y, a) => multI (add X, Y), a
#		# (multI X, a) + (multI, X, b) => multI X, (a + b)
#		# (multI X, a) + (multI, Y, b) => gcd(a, b) * sum(a/d * [X] <U> b/d * [Y])
#		case (expression(op = "multI", ins = [X], const = a), \
#			  expression(op = "multI", ins = [Y], const = b)):
#			assert(not "TODO");
#		
#		
#		
#		# product(A) + product(B) => product(A <I> B) * (product(A - B) + product(B - A))
#		case (multiplicity(op = "product", ins = A), \
#			  multiplicity(op = "product", ins = B)):
##			# take the intersection
##			intersection = multiplicity.intersection(A, B);
##			
##			if len(intersection):
##				AB = multiplicity.difference(A, intersection);
##				BA = multiplicity.difference(B, intersection);
##				
##				if len(AB) == 0:
##					lvn = load_literal(vrtovn, et, 1);
##				elif len(AB) == 1 and AB[0][1] == 1:
##					lvn = AB[0][0];
##				else:
##					lvn = consider_multi(vrtovn, et, "product", AB);
##				
##				if len(BA) == 0:
##					rvn = load_literal(vrtovn, et, 1);
##				elif len(BA) == 1 and BA[0][1] == 1:
##					rvn = BA[0][0];
##				else:
##					rvn = consider_multi(vrtovn, et, "product", BA); 
##				
##				lvn = optimize_add_vr(vrtovn, et, lvn, rvn);
##				
##				rvn = consider_multi(vrtovn, et, "product", intersection);
##				
##				valnum = optimize_mult_vr(vrtovn, et, lvn, rvn, out);
##				
##			else:
##				assert(not "TODO");
#			assert(not "TODO");
#		
#		# X + c => addI X, c
#		
#		# c + X => addI X, c
#		
#		# ∑(X) + Y = ∑(X + [Y]):
#		
#		# Y + ∑(X) = ∑(X + [Y]):
		















