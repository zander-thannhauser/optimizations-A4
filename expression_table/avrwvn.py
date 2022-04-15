
from debug import *;

def expression_table_avrwvn(self, vr, vn):
	enter(f"expression_table.avrwvn(vr = {vr}, vn = {vn})");
	
	self._vrtovn[vr] = vn;
	
	dprint(f"self._vrtovn[{vr}] = {self._vrtovn[vr]}");
	
	exit(f"return {vn};");
	return vn;



