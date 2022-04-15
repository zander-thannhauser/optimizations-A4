
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal, consider;

def optimize_testle_vr(ops, et, ivn, out = None):
	enter(f"optimize_testle_vr(ivn = {ivn}, out = {out})");
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			valnum = load_literal(ops, et, 1 if c <= 0 else 0, out);
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			valnum = consider(ops, et, "cmp_LE", (X, Y), out);
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testle(ops, ins, out, expression_table, **_):
	enter(f"optimize_testle(ins = {ins}, out = {out})");
	
	ivn = expression_table.vrtovn(ins[0]);
	
	optimize_testle_vr(ops, expression_table, ivn, out);
	
	exit("return;");


