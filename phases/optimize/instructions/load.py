
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.expression.self import expression;

from instruction.self import instruction;

from .mult import optimize_mult_vr;

from .common import load_literal;

def optimize_load(ops, vrtovn, ins, out, vnsrcs, avin, expression_table, id, **_):
	enter(f"optimize_load(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	loadex = unknown(id);
	oresult = expression_table.extovn(loadex);
	ovn = oresult.valnum;
	
	if not oresult.is_new:
		loadex = expression_table.vntoex(ovn);
		# assert(not "TODO");
	
	match (expression_table.vntoex(ivn)):
		# load X, (Y + c) => loadAI X -> Y, c
		case expression(op = "addI", ins = [Y], const = c):
			# load = instruction("loadAI", [ivn, Y], const = c, out = ovn);
			assert(not "TODO");
		
		# load X, (Y + Z) => loadAO X -> Y, Z
		case expression(op = "add", ins = [Y, Z]):
			load = instruction("loadAO", [ivn, Y, Z], out = ovn);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			load = instruction("load", [ivn], out = ovn);
			assert(not "TODO");
	
	loadex.instruction = load;
	ops.append(load);
	
	vrtovn[out] = ovn;
	vnsrcs[ovn] = set([load]);
	avin.add(ovn);
	
	exit();
	return [];








