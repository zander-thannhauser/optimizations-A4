
from debug import *;

from .common import load_literal;

def optimize_loadI(vrtovn, const, out, expression_table, **_):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	assert(not "TODO");
	
#	load_literal(vrtovn, expression_table, const, out = out);
	
	exit("return;");
	return [];


