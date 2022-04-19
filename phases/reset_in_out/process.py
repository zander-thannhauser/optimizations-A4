
from debug import *;

from phases.in_out.self import in_out_phase;
from phases.reset_in_out.self import reset_in_out_phase;

def reset_in_out_phase_process(self, all_blocks, parameters, **_):
	enter(f"reset_in_out_phase.process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	ins = None; # set of registers
	outs = list(); # (register, instruction) tuples in *original* order
	
	if block.ins != ins:
		todo.append(in_out_phase(block));
		for parent in block.predecessors:
			todo.append(reset_in_out_phase(parent));
		block.ins = ins;
		
	block.ins = ins;
	block.outs = outs;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















