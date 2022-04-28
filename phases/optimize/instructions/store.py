
from debug import *;

from instruction.self import instruction;

from expression_table.label.self import label;
from expression_table.parameter.self import parameter;
from expression_table.expression.self import expression;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_store(ops, vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_store(ins = {ins}, out = {out})");
	
	ivn, ovn = vrtovn[ins[0]], vrtovn[ins[1]];
	
	match (expression_table.vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case expression(op = "addI", ins = [Y], const = c):
			ops.append(instruction("storeAI", [ivn, Y], const = c));
		
		# store X, (Y + Z) => storeAO X -> Y, Z
		case expression(op = "add", ins = [Y, Z]):
			ops.append(instruction("storeAO", [ivn, Y, Z]));
		
		case label() | parameter():
			ops.append(instruction("store", [ivn, ovn]));
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			# store = (Instruction("store", [ivn, ovn], None));
			assert(not "TODO");
	
	exit("return;");

