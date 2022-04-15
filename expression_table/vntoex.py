
from debug import *;

def expression_table_vntoex(self, vn):
	enter(f"expression_table.vntoex(vn = {vn})");
	exp = self._vntoex.get(vn);
	exit(f"return {exp}");
	return exp;


