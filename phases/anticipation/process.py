
from debug import *;

from phases.anticipation.self import anticipation_phase;

def anticipation_phase_process(self, usage, **_):
	enter(f"anticipation_phase_process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	antout = set();       # set of downwards-exposed instructions
	
	if len(block.successors):
		antout = set.intersection(*(s.antin for s in block.successors if s.antin is not None));
	
	dprint(f"antout = {antout}")
	
	antloc = set();  # instructions
	antkill = set(); # instructions
	
	for inst in block.instructions[::-1]:
		if (out := inst.out):
			if (users := usage.get(out)):
				antloc.difference_update(users);
				antkill.update(users);
			
			if inst.op not in ["i2i", "icall"]:
				antloc.add(out);
		
		# self.subdotout(inst, usage, antloc, antkill);
	
	dprint(f"antloc = {antloc}");
	dprint(f"antkill = {antkill}");
	
	antin = set.union(antloc, set.difference(antout, antkill));
	
	todo = [];
	
	if block.antin != antin:
		for parent in block.predecessors:
			todo.append(anticipation_phase(parent));
	
	block.antloc = antloc;
	block.antout = antout;
	block.antin = antin;
	block.antkill = antkill;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;

















