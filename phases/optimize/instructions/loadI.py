
from debug import *;

from .common import load_literal;

def optimize_loadI(const, out, **stuff):
	enter(f"optimize_loadI(const = {const}, out = {out})");
	
	load_literal(stuff, const, out);
	
	exit("return;");
	return [];


