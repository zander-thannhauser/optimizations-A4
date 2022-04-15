
#from Instruction.self import Instruction;

from expression_table.expression.self import expression;
from expression_table.constant.self import constant;

from debug import *;

def consider(ops, et, op, ins, out = None, const = None):
	enter(f"consider(op = {op}, ins = {ins}, out = {out}, const = {const})");
	
	exp = expression(op = op, ins = ins, const = const);
	
	result = et.extovn(exp);
	
	if out is not None:
		et.avrwvn(out, result.valnum);
	
	exit(f"return {result.valnum}")
	return result.valnum;


def load_literal(ops, et, literal, out = None):
	enter(f"load_literal(literal = {literal})");
	
	result = et.extovn(constant(value = literal));
	
	if out is not None:
		et.avrwvn(out, result.valnum);
	
	exit(f"return {result.valnum};");
	return result.valnum;

