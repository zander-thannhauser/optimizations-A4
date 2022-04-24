
from debug import *;

from instruction.self import instruction;

#from ExpressionTable.Expression.self import Expression;

def optimize_ret(ops, **_):
	enter(f"optimize_ret()");
	
	ret = instruction("ret", []);
	
	ops.append(ret);
	
	exit("return");
