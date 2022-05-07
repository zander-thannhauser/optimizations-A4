
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from .common import consider_exp;
from .common import consider_multi;
from .common import load_literal;

from .add import optimize_add_vr;
from .mult import optimize_mult_vr;

def optimize_sub_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_sub_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(vrtovn, et, a - b, out);
		
		# identities:
		# X - 0 = X
		case (_, constant(value = 0)):
			if out is not None: vrtovn[out] = lvn;
			valnum = lvn;
		
		# X - X = 0
		case (_, _) if lvn == rvn:
			valnum = load_literal(vrtovn, et, 0, out);
		
		# (X + a) - b => X + (a - b):
		case (expression(op = "addI", ins = (X, ), const = a), constant(value = b)):
			if a - b == 0:
				if out is not None: vrtovn[out] = X;
				valnum = X;
			else:
				valnum = consider_exp(vrtovn, et, "addI", (X,), const = a - b, out = out);
		
		# (X + a) - X => a:
		# (X + a) - Y => (X - Y) + a:
		case (expression(op = "addI", ins = (X, ), const = a), phi()):
			if X == rvn:
				assert(not "TODO");
			else:
				subvn = optimize_sub_vr(vrtovn, et, X, rvn);
				valnum = consider_exp(vrtovn, et, "addI", (subvn,), const = a, out = out);
		
		# (X + a) - (Y + b) => (X - Y) + (a - b):
		case (expression(op = "addI", ins = (X, ), const = a),
		      expression(op = "addI", ins = (Y, ), const = b)):
			if X == Y:
				assert(not "TODO");
			elif a == b:
				valnum = optimize_sub_vr(vrtovn, et, X, Y, out = out);
			else:
				sublvn = optimize_sub_vr(vrtovn, et, X, Y);
				valnum = consider_exp(vrtovn, et, "addI", (sublvn,), const = a - b, out = out);
		
		case (parameter() | phi() | unknown(), multiplicity(op = "sum", ins = ins)):
			new = multiplicity.difference([(lvn, 1)], ins);
			dprint(f"new = {new}")
			if len(new) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", new, out);
		
		# X - X * b => X * (1 - b)
		# X - Y * b => ∑(X - b * [Y]):
		case (parameter(), expression(op = "multI", ins = (Y,), const = b)):
			new = multiplicity.difference([(lvn, 1)], [(Y, b)]);
			if len(new) == 1:
				assert(not "TODO");
			else:
				valnum = consider_multi(vrtovn, et, "sum", new, out);
			
		# X * a - X => X * (b - 1)
		# X * a - Y => ∑(a * X - [Y]):
		case (expression(op = "multI", ins = (Y,), const = b), parameter() | phi()):
			new = multiplicity.difference([(Y, b)], [(rvn, 1)]);
			if len(new) == 1:
				term, factor = new[0];
				if factor == 1:
					if out is not None: vrtovn[out] = term;
					valnum = term;
				else:
					assert(not "TODO");
			else:
				# valnum = consider_multi(vrtovn, et, "sum", new, out);
				assert(not "TODO");
		
		# (X + a) - (Y * b) => (X - Y * b) + a:
		case (expression(op = "addI",  ins = (X, ), const = a),
		      expression(op = "multI", ins = (Y, ), const = b)):
			subvn = optimize_sub_vr(vrtovn, et, X, rvn);
			valnum = consider_exp(vrtovn, et, "addI", (subvn,), const = a, out = out);
		
		# X - c => addI X, -c
		case (phi() | multiplicity(op = "sum"), constant(value = c)):
			valnum = consider_exp(vrtovn, et, "addI", (lvn,), const = -c, out = out);
		
		# default:
		case (lex, rex):
			# valnum = consider_multi(vrtovn, et, "sum", sorted([(lvn, 1), (rvn, -1)]), out);
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_sub(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_sub(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_sub_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];






#		
#		# product(A) - product(B) => product(A <I> B) * (product(A - B) - product(B - A))
#		case (multiplicity(op = "product", ins = A), \
#			  multiplicity(op = "product", ins = B)):
#			# subtract the intersection
#			intersection = multiplicity.intersection(A, B);
#			
#			if len(intersection):
#				AB = multiplicity.difference(A, intersection);
#				BA = multiplicity.difference(B, intersection);
#				
#				if len(AB) == 0:
#					lvn = load_literal(vrtovn, et, 1);
#				elif len(AB) == 1 and AB[0][1] == 1:
#					lvn = AB[0][0];
#				else:
#					lvn = consider_multi(vrtovn, et, "product", AB);
#				
#				if len(BA) == 0:
#					rvn = load_literal(vrtovn, et, 1);
#				elif len(BA) == 1 and BA[0][1] == 1:
#					rvn = BA[0][0];
#				else:
#					rvn = consider_multi(vrtovn, et, "product", BA);
#				
#				lvn = optimize_sub_vr(vrtovn, et, lvn, rvn);
#				
#				rvn = consider_multi(vrtovn, et, "product", intersection);
#				
#				valnum = optimize_mult_vr(vrtovn, et, lvn, rvn, out);
#			else:
#				assert(not "TODO");
#		





