
#from Instruction.self import Instruction;

from expression_table.expression.self import expression;
from expression_table.constant.self import constant;

from debug import *;

def consider(ops, vrtovn, avin, et, op, ins, const = None, out = None):
	enter(f"consider_exp(op = {op}, ins = {ins}, const = {const}, out = {out})");
	
	exp = expression(op = op, ins = ins, const = const);
	
	result = et.extovn(exp);
	
	if not result.is_new:
		assert(not "TODO");
	
	if result.valnum not in avin:
		exp.append_instructions(ops, avin, et);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum}")
	return result.valnum;

def load_literal(ops, vrtovn, avin, et, literal, out = None):
	enter(f"load_literal(literal = {literal}, out = {out})");
	
	exp = constant(value = literal);
	
	result = et.extovn(exp);
	
	if not result.is_new:
		exp = et.vntoex(result.valnum);
	
	if result.valnum not in avin:
		exp.append_instructions(ops, avin, et);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum};");
	return result.valnum;
















