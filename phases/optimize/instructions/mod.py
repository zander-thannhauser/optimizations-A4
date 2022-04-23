
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider_multi;
from .common import consider_exp;
from .common import load_literal;

from .mult import optimize_mult_vr;

def optimize_mod_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_mod_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	assert(not "TODO");
	
#	match (et.vntoex(lvn), et.vntoex(rvn)):
#		case (_, _) if lvn == rvn:
#			valnum = load_literal(vrtovn, et, 0, out);
#		
#		case (constant(value = a), constant(value = b)) if b != 0:
#			# return a % b
#			assert(not "TODO");
#		
#		case (_, constant(value = 1)):
#			valnum = load_literal(vrtovn, et, 0, out);
#		
#		case (_, constant(value = -1)):
#			# return 0
#			assert(not "TODO");
#		
#		case (expression(op = "multI", ins = [X], const = a), constant(value = b)):
#			# d = gcd(a, b);
#			# return multI(d, mod(multI((a % b) // d, X), b // d));
#			assert(not "TODO");
#		
#		case (constant(value = a), expression(op = "multI", ins = [X], const = b)):
#			# d = gcd(a, b);
#			# return multI(d, mod(a // d, multI(b // d, X)));
#			assert(not "TODO");
#		
#		case (expression(op = "multI", ins = [X], const = a), \
#		      expression(op = "multI", ins = [Y], const = b)):
#			# d = gcd(a, b);
#			# return multI(d, mod(multI((a % b) // d, X), multI(b // d, X)));
#			assert(not "TODO");
#		
#		case (multiplicity(op = "product", ins = A),
#		      multiplicity(op = "product", ins = B)):
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
#				lvn = optimize_mod_vr(vrtovn, et, lvn, rvn);
#				
#				rvn = consider_multi(vrtovn, et, "product", intersection);
#				
#				valnum = optimize_mult_vr(vrtovn, et, lvn, rvn, out);
#				
#			else:
#				assert(not "TODO");
#		
#		case _:
#			valnum = consider_exp(vrtovn, et, "mod", (lvn, rvn), out);
	
	exit(f"return {valnum};");
	return valnum;

def optimize_mod(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_mod(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_mod_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");
	return [];





















