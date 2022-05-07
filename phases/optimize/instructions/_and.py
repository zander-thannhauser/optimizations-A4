
from debug import *;

from expression_table.constant.self import constant;
from expression_table.unordered.self import unordered;

from .common import consider_un;
from .common import load_literal;

def optimize_and_vr(vrtovn, et, lvn, rvn, out = None):
	enter(f"optimize_and_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		# constant-folding:
		case (constant(value = a), constant(value = b)):
			# retval = load_literal(ops, et, a + b, out);
			assert(not "TODO");
		
		# identities:
		# zero and X = X
		case (constant(value = a), _):
			if a:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# X and 0 = X
		case (_, constant(value = a)):
			if a:
				assert(not "TODO");
			else:
				assert(not "TODO");
		
		# default:
		case (_, _):
			# retval = consider_un(vrtovn, et, "and", set([lvn, rvn]), out);
			assert(not "TODO");
	
	exit(f"return {retval};");
	return retval;


def optimize_and(vrtovn, expression_table, ins, out, label, **_):
	enter(f"optimize_and(ins = {ins}, out = {out})");
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_and_vr(vrtovn, expression_table, lvn, rvn, out);
	
	exit("return;");







#		case (unordered(op = "and", ins = A), unordered(op = "and", ins = B)):
#			assert(not "TODO");
#		
#		case (unordered(op = "and", ins = A), _):
#			together = set.union(A, set([rvn]));
#			retval = consider_un(vrtovn, et, "and", together, out);
#			# for each element:
#				# check that not(element) isn't also in the union
#			assert(not "TODO");
#		
#		case (_, unordered(op = "and", ins = B)):
#			assert(not "TODO");
#		






