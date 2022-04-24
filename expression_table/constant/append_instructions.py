
from debug import *;

from instruction.self import instruction;

def constant_append_instructions(self, ops, avin, et):
	enter("constant_generate_instructions()");
	
	if not self.instruction:
		self.instruction = instruction(\
			"loadI", [], const = self.value, out = self.valnum);
	
	ops.append(self.instruction);
	
	avin.add(self.valnum);
	
	exit();
	

