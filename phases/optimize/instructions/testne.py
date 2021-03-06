
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider;

def optimize_testne_vr(stuff, ivn, out = None):
	enter(f"optimize_testne_vr(ivn = {ivn}, out = {out})");
	
	et = stuff["expression_table"];
	vrtovn = stuff["vrtovn"];
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			# valnum = load_literal(vrtovn, et, 1 if c < 0 else 0, out);
			assert(not "TODO");
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			match (et.vntoex(X), et.vntoex(Y)):
				case (constant(value = 0), _):
					assert(not "TODO");
				case (_, constant(value = 0)):
					if out is not None: vrtovn[out] = X;
					valnum = X;
				case (unknown(), unknown()):
					valnum = consider(stuff, "cmp_NE", (min(X, Y), max(X, Y)), out = out);
				case _:
					assert(not "TODO");
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testne(ins, out, **stuff):
	enter(f"optimize_testne(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	optimize_testne_vr(stuff, ivn, out);
	
	exit("return;");


