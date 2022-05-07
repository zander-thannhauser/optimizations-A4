
from debug import *;

from expression_table.unknown.self import unknown;
from expression_table.constant.self import constant;
from expression_table.expression.self import expression;

from .common import load_literal;
from .common import consider_exp;

def optimize_testne_vr(vrtovn, et, ivn, out = None):
	enter(f"optimize_testne_vr(ivn = {ivn}, out = {out})");
	
	match (et.vntoex(ivn)):
		# constant-fold:
		case constant(value = c):
			valnum = load_literal(vrtovn, et, 1 if c != 0 else 0, out);
		
		# substitutions:
		case expression(op = "comp", ins = [X, Y]):
			match (et.vntoex(X), et.vntoex(Y)):
				case (unknown(), unknown()):
					valnum = consider_exp(vrtovn, et, "cmp_NE", ins = (X, Y), out = out);
				case (lex, rex):
					dprint(f"(lex, rex) = {(str(lex), str(rex))}")
					assert(not "TODO");
		
		# default:
		case (iex):
			assert(not "TODO");
	
	exit(f"return {valnum}");
	return valnum;

def optimize_testne(vrtovn, ins, out, expression_table, **_):
	enter(f"optimize_testne(ins = {ins}, out = {out})");
	
	ivn = vrtovn[ins[0]];
	
	optimize_testne_vr(vrtovn, expression_table, ivn, out);
	
	exit("return;");


