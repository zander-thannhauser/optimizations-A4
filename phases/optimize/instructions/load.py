
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.expression.self import expression;
from expression_table.multiplicity.self import multiplicity;

from instruction.self import instruction;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_load(ops, vrtovn, ins, out, expression_table, id, **_):
	enter(f"optimize_load(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	loadex = unknown(id);
	oresult = expression_table.extovn(loadex);
	ovn = oresult.valnum;
	
	match (expression_table.vntoex(ivn)):
		# load X, (Y + c) => loadAI X -> Y, c
		case expression(op = "addI", ins = [X], const = c):
			load = instruction("loadAI", ins = (X, ), const = c, out = ovn);
		
		# load X, (Y + c) => loadAI X -> Y, c
		case multiplicity(op = "sum", ins = ins) if len(ins) == 2:
			sublvn, sublfactor = ins[0]
			subrvn, subrfactor = ins[1]
			et = expression_table;
			lvn = optimize_mult_vr(vrtovn, et, sublvn, load_literal(vrtovn, et, sublfactor));
			rvn = optimize_mult_vr(vrtovn, et, subrvn, load_literal(vrtovn, et, subrfactor));
			load = instruction("loadAO", ins = (min(lvn, rvn), max(lvn, rvn)), out = ovn);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
#			load = instruction("load", [ivn], out = ovn);
			assert(not "TODO");
	
	loadex.instruction = load;
	ops.append(load);
	
	vrtovn[out] = ovn;
	
	exit();
	return [];








