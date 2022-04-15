
from debug import *;

from instruction.self import instruction;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

def optimize_cbrne(ops, ins, out, expression_table, volatile, label, **_):
	enter(f"optimize_cbrne(ins = {ins}, out = {out})");
	
	dprint(f"volatile = {volatile}")
	
	ivn = expression_table.vrtovn(ins[0]);
	
	match (expression_table.vntoex(ivn)):
		# constant-folding:
		case constant(value = c):
#			if not c: ops.append(Instruction("jumpI", [], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_LT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			ops.append(instruction("cbr_GE", [X, Y], out, label = label));
		
		case expression(op = "cmp_LE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "cmp_GT", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "cmp_EQ", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
#			ops.append(Instruction("cbr_NE", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "cmp_NE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
#			ops.append(Instruction("cbr_EQ", [X, Y], out, label));
			assert(not "TODO");
		
		case expression(op = "testeq", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "testne", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "testgt", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "testge", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "testlt", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "testle", ins = [X]) \
			if X not in volatile:
			assert(not "TODO");
		
		case expression(op = "and", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "or", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			assert(not "TODO");
		
		case expression(op = "not", ins = [X]) \
			if X not in volatile:
#			ops.append(Instruction("cbr", [X], out, label));
			assert(not "TODO");
		
		# default:
		case (iex):
			dprint(f"iex == {iex}");
			# ops.append(Instruction("cbr", [ivn], out));
			ops.append(instruction("cbrne", [ivn], out, label = label));
	
	
	exit("return;");
	return [];













