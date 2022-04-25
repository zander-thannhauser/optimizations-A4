
from debug import *;

from phases.allocate_register.self import allocate_register_phase;
from phases.liveids_to_register.self import liveids_to_register_phase;

def allocate_register_phase_process(self, num_registers, interference, **_):
	enter(f"allocate_register.process(self.liverange = {self.liverange})");
	
	lr = self.liverange;
	
	dprint(f"lr = {lr}")
	
	taken = set();
	
	for i in interference:
		if lr == i[0] and i[1].register is not None:
			taken.add(i[1].register);
		elif lr == i[1] and i[0].register is not None:
			taken.add(i[0].register);
	
	dprint(f"taken = {taken}")
	
	available = set.difference(set(range(num_registers)), taken);
	
	dprint(f"available = {available}")
	
	todo = [];
	
	if len(available):
		lr.register = min(available);
		todo.append(liveids_to_register_phase(lr));
	else:
		assert(not "TODO");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















