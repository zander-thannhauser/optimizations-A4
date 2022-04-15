
from debug import *;

def expression_table_vrtovn(self, vr):
	enter(f"expression_table_vrtovn(vr = {vr})");
	valnum = self._vrtovn[vr];
	exit(f"return {valnum};")
	return valnum;

