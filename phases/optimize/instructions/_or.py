
from debug import *;

from expression_table.constant.self import constant;
from expression_table.unordered.self import unordered;

from .common import consider_un;
from .common import load_literal;

def optimize_or_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_or_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
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
		
		case (unordered(op = "or", ins = A), unordered(op = "or", ins = B)):
			assert(not "TODO");
		
		case (unordered(op = "or", ins = A), _):
			together = set.union(A, set([rvn]));
			retval = consider_un(vrtovn, et, "or", together, out);
			# for each element:
				# check that not(element) isn't also in the union
			assert(not "TODO");
		
		case (_, unordered(op = "or", ins = B)):
			assert(not "TODO");
		
		# default:
		case (_, _):
			retval = consider_un(vrtovn, et, "or", set([lvn, rvn]), out);
	
	exit(f"return {retval};");
	return retval;


def optimize_or(vrtovn, expression_table, ins, out, label, **_):
	enter(f"optimize_or(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_or_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");













