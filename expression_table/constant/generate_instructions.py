
from debug import *;

from instruction.self import instruction;

def constant_generate_instructions(self, valnum, expression_table, ops):
	enter("constant_generate_instructions()");
	
	if not self.instruction:
		self.instruction = instruction(op = "loadI", ins = [], const = self.value, out = valnum);
		ops.append(self.instruction);
	
	exit();

