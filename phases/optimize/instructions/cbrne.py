
from debug import *;

from instruction.self import instruction;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

def optimize_cbrne_vn(ops, ivn, et, volatile, label, **_):
	enter(f"optimize_cbrne_vn(ivn = {ivn}, volatile = {volatile})");
	
	match (et.vntoex(ivn)):
		# constant-folding:
		case constant(value = c):
			if not c: ops.append(instruction("jumpI", [], label = label));
		
		case expression(op = "cmp_LT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(instruction("cbr_GE", [X, Y], label = label));
		
		case expression(op = "cmp_LE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(Instruction("cbrne_LE", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_GT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(instruction("cbrne_GT", [X, Y], out, label = label));
			assert(not "TODO");
		
		case expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(Instruction("cbrne_GE", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_EQ", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbrne_EQ", [X, Y], "->", outs));
			assert(not "TODO");
		
		case expression(op = "cmp_NE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			# ops.append(("cbrne_NE", [X, Y], "->", outs));
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
			# ops.append(Instruction("cbrnene", [X], out, label));
			assert(not "TODO");
		
		# default:
		case iex:
			# ops.append(instruction("cbrne", [ivn], out, label = label));
			assert(not "TODO");

	exit("return;");
	return [];


def optimize_cbrne(ops, vrtovn, ins, expression_table, volatile, label, **_):
	enter(f"optimize_cbrne(ins = {ins}, volatile = {volatile})");
	
	ivn = vrtovn[ins[0]];
	
	optimize_cbrne_vn(ops, ivn, expression_table, volatile, label);
	
	exit("return;");
	return [];























