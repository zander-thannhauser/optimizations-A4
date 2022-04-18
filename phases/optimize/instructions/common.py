
#from Instruction.self import Instruction;

from expression_table.expression.self import expression;
from expression_table.unordered.self import unordered;
from expression_table.multiplicity.self import multiplicity;
from expression_table.constant.self import constant;

from debug import *;

def consider_exp(vrtovn, et, op, ins, out = None, const = None):
	enter(f"consider_exp(op = {op}, ins = {ins}, out = {out}, const = {const})");
	
	exp = expression(op = op, ins = ins, const = const);
	
	result = et.extovn(exp);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum}")
	return result.valnum;


def consider_multi(vrtovn, et, op, ins, out = None):
	enter(f"consider_multi(op = {op}, ins = {ins}, out = {out})");
	
	exp = multiplicity(op = op, ins = ins);
	
	result = et.extovn(exp);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum}")
	return result.valnum;


def consider_un(vrtovn, et, op, ins, out = None):
	enter(f"consider_un(op = {op}, ins = {ins}, out = {out})");
	
	exp = unordered(op = op, ins = ins);
	
	result = et.extovn(exp);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum}")
	return result.valnum;


def load_literal(vrtovn, et, literal, out = None):
	enter(f"load_literal(literal = {literal}, out = {out})");
	
	result = et.extovn(constant(value = literal));
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum};");
	return result.valnum;
















