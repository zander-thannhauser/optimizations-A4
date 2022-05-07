
from debug import *;

from instruction.self import instruction;

from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_store(ops, vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_store(ins = {ins}, out = {out})");
	
	ivn, ovn = vrtovn[ins[0]], vrtovn[ins[1]];
	
	match (expression_table.vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case expression(op = "addI", ins = [X], const = c):
			store = instruction("storeAI", ins = (ivn, X), const = c);
		
		# store X, (Y + c) => storeAI X -> Y, c
		case multiplicity(op = "sum", ins = ins) if len(ins) == 2:
			sublvn, sublfactor = ins[0]
			subrvn, subrfactor = ins[1]
			et = expression_table;
			lvn = optimize_mult_vr(vrtovn, et, sublvn, load_literal(vrtovn, et, sublfactor));
			rvn = optimize_mult_vr(vrtovn, et, subrvn, load_literal(vrtovn, et, subrfactor));
			store = instruction("storeAO", [ivn, min(lvn, rvn), max(lvn, rvn)]);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			# store = (Instruction("store", [ivn, ovn], None));
			assert(not "TODO");
	
	ops.append(store);
	
	exit("return;");

