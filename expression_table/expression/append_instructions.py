
#from debug import *;

#from instruction.self import instruction;

#def expression_append_instructions(self, ops, et, avin, vnsrcs):
#	enter("expression_generate_instructions()");
#	
#	for subvn in self.ins:
#		if subvn not in avin:
#			subex = et.vntoex(subvn);
#			subex.append_instructions(ops, avin, et);
#	
#	if not self.instruction:
#		self.instruction = instruction( \
#			op = self.op, \
#			ins = self.ins, \
#			const = self.const, \
#			out = self.valnum);
#		dprint(f"self.instruction = {self.instruction}");
#	
#	assert(not "TODO");
#	ops.append(self.instruction);
#	
#	avin.add(self.valnum);
#	
#	exit();
#	

