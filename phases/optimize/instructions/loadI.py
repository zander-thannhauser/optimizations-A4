
from debug import *;

from .common import load_literal;

def optimize_loadI(ops, vrtovn, avin, const, out, expression_table, **_):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	load_literal(ops, vrtovn, avin, expression_table, literal = const, out = out);
	
	exit("return;");
	return [];


