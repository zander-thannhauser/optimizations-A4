
from debug import *;

from instruction.self import instruction;

from expression_table.expression.self import expression;

from phases.critical.self import critical_phase;

def optimize_store(ops, ins, out, expression_table, todo, **_):
	enter(f"optimize_store(ins = {ins}, out = {out})");
	
	ivn = expression_table.vrtovn(ins[0]);
	ovn = expression_table.vrtovn(ins[1]);
	
	match (expression_table.vntoex(ovn)):
		# store X, (Y + c) => storeAI X -> Y, c
		case expression(op = "addI", ins = [X], const = c):
			store = instruction("storeAI", [ivn, X], None, const = c);
		
		# store X, (Y + Z) => storeAO X -> Y, Z
		case expression(op = "add", ins = [X, Y]):
			store = instruction("storeAO", [ivn, X, Y], None);
		
		# default:
		case (oexp):
			dprint(f"oexp == {oexp}");
			# ops.append(Instruction("store", [ivn, ovn], None));
			assert(not "TODO");
	
	store.is_critical = True;
	todo.append(critical_phase(store));
	
	ops.append(store);
	
	exit("return;");

