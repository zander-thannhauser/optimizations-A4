
from instruction.self import instruction;

from expression_table.expression.self import expression;
from expression_table.constant.self import constant;

from debug import *;

def load_literal(stuff, literal, out = None):
	enter(f"load_literal(literal = {literal}, out = {out})");
	
	ops = stuff["ops"];
	vrtovn = stuff["vrtovn"];
	avin = stuff["avin"];
	et = stuff["expression_table"];
	
	exp = constant(value = literal);
	
	result = et.extovn(exp);
	
	if not result.is_new:
		exp = et.vntoex(result.valnum);
	
	if result.valnum not in avin:
		new = instruction(op = "loadI", ins = [], const = exp.value, out = exp.valnum);
		dprint(f"new = {new}")
		avin.add(result.valnum);
		ops.append(new);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum};");
	return result.valnum;


def consider(stuff, op, ins, const = None, out = None):
	enter(f"consider_exp(op = {op}, ins = {ins}, const = {const}, out = {out})");
	
	ops = stuff["ops"];
	vrtovn = stuff["vrtovn"];
	avin = stuff["avin"];
	et = stuff["expression_table"];
	
	exp = expression(op = op, ins = ins, const = const);
	
	result = et.extovn(exp);
	
	if not result.is_new:
		exp = et.vntoex(result.valnum);
	
	if result.valnum not in avin:
		new = instruction(op = exp.op, ins = exp.ins, const = exp.const, out = exp.valnum);
		dprint(f"new = {new}")
		avin.add(result.valnum);
		ops.append(new);
	
	if out is not None:
		vrtovn[out] = result.valnum;
	
	exit(f"return {result.valnum}")
	return result.valnum;

def s(x):
	return u(x + (1 << 31)) - (1 << 31);

def u(x):
	limit = 1 << 32
	while x < 0: x += limit;
	while x > limit: x -= limit;
	return x;












































