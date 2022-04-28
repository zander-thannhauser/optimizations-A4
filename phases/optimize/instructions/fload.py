
from debug import *;

from expression_table.label.self import label;
from expression_table.unknown.self import unknown;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from instruction.self import instruction;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_fload(ops, vrtovn, ins, out, avin, expression_table, id, **_):
	enter(f"optimize_fload(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	loadex = unknown(id);
	oresult = expression_table.extovn(loadex);
	ovn = oresult.valnum;
	
	if not oresult.is_new:
		loadex = expression_table.vntoex(ovn);
	
	match (expression_table.vntoex(ivn)):
		# fload X, (Y + c) => floadAI X -> Y, c
		case expression(op = "addI", ins = (Y, ), const = c):
			fload = instruction("floadAI", [Y], const = c, out = ovn);
			assert(not "CHECK");
		
		# fload (X + Y) -> Z => floadAO X, Y -> Z
		case expression(op = "add", ins = (X, Y)):
			fload = instruction("floadAO", [X, Y], out = ovn);
			assert(not "CHECK");
		
		case label() | parameter():
			fload = instruction("fload", [ivn], out = ovn);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			fload = instruction("fload", [ivn], out = ovn);
			assert(not "TODO");
	
	loadex.instruction = fload;
	ops.append(fload);
	
	vrtovn[out] = ovn;
	avin.add(ovn);
	
	exit();
	return [];








