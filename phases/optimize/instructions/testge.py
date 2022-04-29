
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider;

def optimize_testge_vr(stuff, ivn, out = None):
	enter(f"optimize_testge_vr(ivn = {ivn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			valnum = load_literal(stuff, 1 if c >= 0 else 0, out);
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			match (et.vntoex(X), et.vntoex(Y)):
				case (constant(value = 0), _):
					assert(not "TODO");
				case (_, constant(value = 0)):
					assert(not "TODO");
				case _:
					valnum = consider(stuff, "cmp_LE", (Y, X), out = out);
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testge(ins, out, **stuff):
	enter(f"optimize_testge(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	optimize_testge_vr(stuff, ivn, out);
	
	exit("return;");


