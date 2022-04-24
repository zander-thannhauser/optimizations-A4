
from debug import *;

from instruction.self import instruction;

from expression_table.expression.self import expression;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_store(ops, vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_store(ins = {ins}, out = {out})");
	
	ivn, ovn = vrtovn[ins[0]], vrtovn[ins[1]];
	
	match (expression_table.vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case expression(op = "addI", ins = [X], const = c):
			store = instruction("storeAI", [ivn, X], const = c);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			# store = (Instruction("store", [ivn, ovn], None));
			assert(not "TODO");
	
	ops.append(store);
	
	exit("return;");

