
from debug import *;

from instruction.self import instruction;

from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

def optimize_cbr_vn(stuff, ivn, volatile, label):
	enter(f"optimize_cbr_vn(ivn = {ivn}, volatile = {volatile})");
	
	ops = stuff["ops"];
	et = stuff["expression_table"];
	
	match (et.vntoex(ivn)):
		# constant-folding:
		case constant(value = c):
			if c: cbr = instruction("jumpI", [], label = label);
			else: cbr = None;
		
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
			cbr = instruction("cbr_GT", [X, Y], label = label);
		
		case expression(op = "cmp_GE", ins = [X, Y]) \
			if X not in volatile and Y not in volatile:
			cbr = instruction("cbr_GE", [X, Y], label = label);
		
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
			cbr = instruction("cbr", [ivn], label = label);
	
	if cbr is not None:
		vnsrcs = stuff["vnsrcs"];
		cbr.subcriticals = set.union(*(vnsrcs[i] for i in cbr.ins));
		ops.append(cbr);
	
	exit("return;");
	return [];


def optimize_cbr(ins, label, **stuff):
	volatile = stuff["volatile"];
	enter(f"optimize_cbr(ins = {ins}, volatile = {volatile})");
	
	vrtovn = stuff["vrtovn"];
	
	ivn = vrtovn[ins[0]];
	
	optimize_cbr_vn(stuff, ivn, volatile, label);
	
	exit("return;");
	return [];























