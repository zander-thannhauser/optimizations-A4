
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider;

def optimize_testgt_vr(stuff, ivn, out = None):
	enter(f"optimize_testgt_vr(ivn = {ivn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			valnum = load_literal(stuff, 1 if c > 0 else 0, out);
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			match (et.vntoex(X), et.vntoex(Y)):
				case (constant(value = 0), _):
					assert(not "TODO");
				case (_, constant(value = 0)):
					assert(not "TODO");
				case (unknown() | phi() | constant(), unknown() | constant() | phi()):
					valnum = consider(stuff, "cmp_LT", (Y, X), out = out);
				case _:
					assert(not "TODO");
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testgt(ins, out, **stuff):
	enter(f"optimize_testgt(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	optimize_testgt_vr(stuff, ivn, out);
	
	exit("return;");


