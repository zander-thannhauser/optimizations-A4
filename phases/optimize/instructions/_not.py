
from debug import *;

from expression_table.phi.self import phi;
from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider;

def optimize_not_vr(stuff, ivn, out = None):
	enter(f"optimize_not_vr(ivn = {ivn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(ivn)):
		# constant-folding:
		case (constant(value = a)):
			# retval = load_literal(ops, et, a + b, out);
			assert(not "TODO");
		
		case (expression(op = "not", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testne", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testeq", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testge", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testgt", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testle", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "testlt", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_ne", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_eq", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_ge", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_gt", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_le", ins = A)):
			assert(not "TODO");
		
		case (expression(op = "cmp_lt", ins = A)):
			assert(not "TODO");
		
		case unknown() | phi() | expression(op = "f2i" | "or" | "and"):
			valnum = consider(stuff, "not", (ivn,), out = out);
		
		case (iex):
			dprint(f"iex = {iex}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;


def optimize_not(vrtovn, expression_table, ins, out, label, **_):
	enter(f"optimize_not(ins = {ins}, out = {out})");
	
	assert(not "TODO");
	
	ivn = vrtovn[ins[0]]
	
	optimize_not_vr(vrtovn, expression_table, ivn, out);
	
	exit("return;");













