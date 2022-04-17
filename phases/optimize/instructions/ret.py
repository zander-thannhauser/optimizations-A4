
from debug import *;

from instruction.self import instruction;

#from ExpressionTable.Expression.self import Expression;

def optimize_ret(ops, ins, out, expression_table, label, **_):
	enter(f"optimize_ret(ins = {ins}, out = {out})");
	
	assert(not "TODO");
	
#	ret = instruction("ret", [], None)
#	ret.is_critical = True;
#	ops.append(ret);
	
	exit("return");
