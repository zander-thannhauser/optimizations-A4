
from debug import *;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;

def optimize_testge_vr(ops, vrtovn, avin, et, ivn, out = None):
	enter(f"optimize_testge_vr(ivn = {ivn}, out = {out})");
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			valnum = load_literal(ops, vrtovn, avin, et, 1 if c >= 0 else 0, out);
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			# valnum = consider(ops, et, "cmp_GE", (X, Y), out);
			assert(not "TODO");
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testge(ops, vrtovn, avin, ins, out, expression_table, **_):
	enter(f"optimize_testge(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	optimize_testge_vr(ops, vrtovn, avin, expression_table, ivn, out);
	
	exit("return;");


