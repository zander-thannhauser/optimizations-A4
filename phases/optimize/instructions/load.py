
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.expression.self import expression;
from instruction.self import instruction;

def optimize_load(ops, ins, out, expression_table, **_):
	enter(f"optimize_load(ins = {ins}, out = {out})");
	
	assert(not "TODO");
	
#	ivn = expression_table.vrtovn(ins[0]);
#	
#	loadex = unknown();
#	oresult = expression_table.extovn(loadex);
#	ovn = oresult.valnum;
#	
#	match (expression_table.vntoex(ivn)):
#		# load (addI X, c) => Y === loadAI X, c => Y
#		case expression(op = "addI", ins = [X], const = c):
#			# ops.append(instruction("loadAI", [X, c], ovn));
#			assert(not "TODO");
#		
#		# load (add  X, Y) => Z === loadAO X, Y => Z
#		case expression(op = "add", ins = [X, Y]):
#			load = instruction("loadAO", [X, Y], ovn);
#		
#		case iex:
#			# dprint(f"iex = {iex}");
#			# ops.append(Instruction("load", [ivn], ovn));
#			assert(not "TODO");
#	
#	loadex.instruction = load;
#	ops.append(load);
#	
#	expression_table.avrwvn(out, ovn);
	
	exit();
	return [];


