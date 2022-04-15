
from debug import *;

from expression_table.self import expression_table;

class expression_table_extovn_retval:
	def __init__(self, valnum, is_new):
		self.valnum = valnum;
		self.is_new = is_new;
	def __str__(self):
		return f"(.valnum = {self.valnum}, .is_new = {self.is_new})";

def expression_table_extovn(self, expression):
	enter(f"expression_table.extovn(expression = {expression})");
	
	if expression in self._extovn:
		valnum = self._extovn[expression];
		is_new = False;
	else:
		valnum = expression_table.valcounter;
		is_new = True;
		self._extovn[expression] = valnum;
		self._vntoex[valnum] = expression;
		expression_table.valcounter += 1;
	
	retval = expression_table_extovn_retval(valnum, is_new);
	
	exit(f"return {str(retval)}");
	return retval;




