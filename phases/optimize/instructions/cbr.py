
from debug import *;

from instruction.self import instruction;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

def optimize_cbr(ops, ins, out, expression_table, volatile, label, **_):
	enter(f"optimize_cbr(ins = {ins}, out = {out}, volatile = {volatile})");
	
	ivn = expression_table.vrtovn(ins[0]);
	
	match (expression_table.vntoex(ivn)):
		# constant-folding:
		case constant(value = c):
			if c: ops.append(instruction("jumpI", [], None, label = label));
		
		case expression(op = "cmp_LT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(Instruction("cbr_LT", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_LE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(Instruction("cbr_LE", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_GT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(instruction("cbr_GT", [X, Y], out, label = label));
		
		case expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(Instruction("cbr_GE", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_EQ", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbr_EQ", [X, Y], "->", outs));
			assert(not "TODO");
		
		case expression(op = "cmp_NE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbr_NE", [X, Y], "->", outs));
			assert(not "TODO");
		
		case expression(op = "testeq", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "testne", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "testgt", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "testge", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "testlt", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "testle", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "not", ins = [X]) \
			if X not in volatile:
			# ops.append(Instruction("cbrne", [X], out, label));
			assert(not "TODO");
		
		# default:
		case iex:
			ops.append(instruction("cbr", [ivn], out, label = label));

	exit("return;");
	return [];


