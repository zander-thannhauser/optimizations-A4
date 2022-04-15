
from debug import *;

from instruction.self import instruction;

def expression_generate_instructions(self, valnum, expression_table, ops):
	enter("expression_generate_instructions()");
	
	if not self.instruction:
		for subvalnum in self.ins:
			subex = expression_table.vntoex(subvalnum);
			subex.generate_instructions(subvalnum, expression_table, ops);
		
		self.instruction = instruction(
			op = self.op,
			ins = self.ins,
			const = self.const,
			out = valnum);
		
		ops.append(self.instruction);
	
	exit();

