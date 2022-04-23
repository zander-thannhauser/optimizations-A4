
from debug import *;

from expression_table.constant.self import constant;

def optimize_assert(vrtovn, ins, expression_table, **_):
	enter(f"optimize_assert(ins = {ins})");
	
	assert(not "TODO");
	
#	ivn = vrtovn[ins[0]];
#	exp = expression_table.vntoex(ivn);
#	
#	dprint(f"{exp}");
#	
#	match exp:
#		case constant(value = c):
#			assert(c);
#		
#		case _:
#			assert(not "TODO");
	
	exit("return;");


