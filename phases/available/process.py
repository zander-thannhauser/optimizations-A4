
from debug import *;

from phases.available.self import available_phase;

def available_phase_process(self, usage, **_):
	enter(f"available_phase_process(block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	avout = set();       # set of downwards-exposed instructions
	
	if len(block.predecessors):
		avout = set.intersection(*(p.avin for p in block.predecessors if p.avin is not None));
	
	dprint(f"avout = {avout}")
	
	avloc = set();  # instructions
	avkill = set(); # instructions
	
	for inst in block.original_instructions:
		if (out := inst.out):
			if (users := usage.get(out)):
				avloc.difference_update(users);
				avkill.update(users);
			
			if inst.op not in ["i2i", "icall"]:
				avloc.add(out);
		
		self.subdotout(inst, usage, avloc, avkill);
	
	dprint(f"avloc = {avloc}");
	dprint(f"avkill = {avkill}");
	
	avin = set.union(avloc, set.difference(avout, avkill));
	
	todo = [];
	
	if block.avin != avin:
		for child in block.successors:
			todo.append(available_phase(child));
	
	block.avloc = avloc;
	block.avout = avout;
	block.avin = avin;
	block.avkill = avkill;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















