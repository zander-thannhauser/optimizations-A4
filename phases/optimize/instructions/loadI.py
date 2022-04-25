
from debug import *;

from .common import load_literal;

def optimize_loadI(const, out, **stuff):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	if type(const) is int:
		load_literal(stuff, const, out);
	else:
		assert(not "TODO");
	
	exit("return;");
	return [];


