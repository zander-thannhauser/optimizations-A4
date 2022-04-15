
from expression_table.self import expression_table;

def expression_table_copy(self):
	
	copy = expression_table();
	
	copy._vntoex = self._vntoex.copy();
	copy._vrtovn = self._vrtovn.copy();
	copy._extovn = self._extovn.copy();
	
	return copy;


