
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;

from .common import consider;
from .common import load_literal;

def optimize_or_vr(stuff, lvn, rvn, out = None):
	enter(f"optimize_or_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			# retval = load_literal(ops, et, a + b, out);
			assert(not "TODO");
		
		# identities:
		# zero or X = X
		case (constant(value = a), _):
			if a:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# X or 0 = X
		case (_, constant(value = a)):
			if a:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		case (_, _) if lvn == rvn:
			assert(not "TODO");
		
		case (unknown(), unknown()):
			valnum = consider(stuff, "or", (min(lvn, rvn), max(lvn, rvn)), out = out);
		
		# ( X or !Y) =>  (X >= Y)
		# (!X or  Y) =>  (X <= Y)
		# (!X or !Y) => !(X and Y)
		
		# default:
		case (_, _):
			# retval = consider_un(vrtovn, et, "or", set([lvn, rvn]), out);
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;


def optimize_or(ins, out, label, **stuff):
	enter(f"optimize_or(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_or_vr(stuff, lvn, rvn, out);
	
	exit("return;");













