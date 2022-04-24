
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider;

def optimize_testeq_vr(stuff, ivn, out = None):
	enter(f"optimize_testeq_vr(ivn = {ivn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			# valnum = load_literal(vrtovn, et, 1 if c == 0 else 0, out);
			assert(not "TODO");
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			valnum = consider(stuff, "cmp_GE", (X, Y), out = out);
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testeq(ins, out, **stuff):
	enter(f"optimize_testeq(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	optimize_testeq_vr(stuff, ivn, out);
	
	exit("return;");


