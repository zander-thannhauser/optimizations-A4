
from debug import *;

from expression_table.phi.self import phi;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from .common import load_literal;
from .common import consider_multi;
from .common import consider_exp;

def optimize_mult_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_mult_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(vrtovn, et, a * b, out);
			
		# identities:
		# 0 * X = 0
		case (constant(value = 0), _):
#			valnum = load_literal(vrtovn, et, 0, out);
			assert(not "TODO");
		
		# 1 * X = X
		case (constant(value = 1), _):
			# avrwvn(out, rvn);
			assert(not "TODO");
		
		# X * 0 = 0
		case (_, constant(value = 0)):
#			valnum = load_literal(vrtovn, et, 0, out);
			assert(not "TODO");
		
		# X * 1 = X
		case (_, constant(value = 1)):
			if out is not None: vrtovn[out] = lvn;
			valnum = lvn;
		
		# (X + a) * b => X * b + (a * b):
		case (expression(op = "addI", ins = (X, ), const = a), constant(value = b)):
			subvn = optimize_mult_vr(vrtovn, et, X, rvn);
			valnum = consider_exp(vrtovn, et, "addI", ins = (subvn, ), const = (a * b), out = out);
		
		# (X * a) * b => X * (a * b):
		case (expression(op = "multI", ins = (X, ), const = a), constant(value = b)):
			valnum = consider_exp(vrtovn, et, "multI", ins = (X, ), const = (a * b), out = out);
		
		case (multiplicity(op = "sum", ins = ins), constant(value = a)):
			valnum = consider_multi(vrtovn, et, "sum", [(v, f * a) for v, f in ins], out);
		
		# mult X, c => multI X, c:
		case (phi(), constant(value = c)):
			valnum = consider_exp(vrtovn, et, "multI", (lvn, ), const = c, out = out);
		
		case (constant(value = c), phi()):
			valnum = consider_exp(vrtovn, et, "multI", (rvn, ), const = c, out = out);
		
		case (phi(), phi()):
			# valnum = consider_multi(vrtovn, et, "product", sorted([(lvn, 1), (rvn, 1)]), out);
			assert(not "TODO");
		
		# default:
		case (lex, rex):
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_mult(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_mult(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_mult_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];




#		# X * -1 = -X
#		case (_, constant(value = -1)):
#			assert(not "TODO");
#		
#		case (_, _) if lvn == rvn:
#			valnum = consider_multi(vrtovn, et, "product", [(lvn, 2)], out);
#		
##		# substitutions:
#		# (addI X, a) * b => addI (multI X, b), (a * b)
#		case (expression(op = "addI", ins = [X], const = a), constant(value = b)):
#			if a * b != 0:
#				subvn = consider_exp(vrtovn, et, "multI", ins = (X, ), const = b);
#				valnum = consider_exp(vrtovn, et, "addI", ins = (subvn, ), const = (a * b), out = out);
#			else:
#				assert(not "TODO");
#		
#		# a * (addI X, b) => addI (multI X, a), (a * b)
#		case (constant(value = a), expression(op = "addI", ins = [X], const = b)):
#			subvn = optimize_mult_vr(vrtovn, et, X, lvn)
#			valnum = consider_exp(vrtovn, et, "addI", (subvn, ), const = a * b, out = out);
#		
#		# (multI X, a) * b => multI X, (a * b)
#		case (expression(op = "multI", ins = [X], const = a), constant(value = b)):
##			consider(ops, et, "multI", (X, a * b), out);
#			assert(not "TODO");
#		
#		# a * (multI X, b) => multI X, (a * b)
#		case (constant(value = a), expression(op = "multI", ins = [X], const = b)):
#			assert(not "TODO");
#		
#		# (multI X, a) * (multI Y, b) => multI (mult X Y), (a * b)
#		case (expression(op = "multI", ins = [X], const = a), \
#		      expression(op = "multI", ins = [Y], const = b)):
#			assert(not "TODO");
#		
#		case (multiplicity(op = "product", ins = A),
#		      multiplicity(op = "product", ins = B)):
#			assert(not "TODO");
#		
#		case (multiplicity(op = "product", ins = A), _):
#			union = multiplicity.union(A, [(rvn, 1)]);
#			if len(union) == 1:
#				assert(not "TODO");
#			else:
#				valnum = consider_multi(vrtovn, et, "product", union, out);
#			
#		case (_, multiplicity(op = "product", ins = A)):
#			union = multiplicity.union([(lvn, 1)], A);
#			if len(union) == 1:
#				assert(not "TODO");
#			else:
#				valnum = consider_multi(vrtovn, et, "product", union, out);
#		
#		# mult c, X => multI X, c:
#		case (constant(value = c), _):
##			consider(ops, et, "multI", (rvn, c), out);
#			assert(not "TODO");
#		


