
from debug import *;

from expression_table.phi.self import phi;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import consider;
from .common import load_literal;

def optimize_rshift_vr(stuff, lvn, rvn, out = None):
	enter(f"optimize_rshift_vr(lvn = {lvn}, rvn = {rvn}, out = {out})");
	
	et = stuff["expression_table"];
	
	match (et.vntoex(lvn), et.vntoex(rvn)):
		
		# a >> b => (a >> b)
		case (constant(value = a), constant(value = b)):
			valnum = load_literal(stuff, a >> b, out);
		
		# identities:
		# 0 >> X = 0
		case (constant(value = 0), _):
			assert(not "TODO");
		
		# X >> 0 = X
		case (_, constant(value = 0)):
			assert(not "TODO");
		
		# rshift X, c => rshiftI X, c:
		case (_, constant(value = c)):
			valnum = consider(stuff, "rshiftI", (lvn, ), const = c, out = out);
		
		case (lex, rex):
			dprint(f"lex, rex = {str(lex), str(rex)}");
			assert(not "TODO");
	
	exit(f"return {valnum};");
	return valnum;

def optimize_rshift(ins, out, **stuff):
	enter(f"optimize_rshift(ins = {ins}, out = {out})");
	
	vrtovn = stuff["vrtovn"];
	
	lvn, rvn = vrtovn[ins[0]], vrtovn[ins[1]]
	
	optimize_rshift_vr(stuff, lvn, rvn, out);
	
	exit("return;");
	return [];






