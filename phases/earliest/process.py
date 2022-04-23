
from debug import *;

from phases.earliest.self import earliest_phase;

def earliest_phase_process(self, start, phase_counters, earliest, **_):
	enter(f"earliest_phase_process(block.po = {self.block.po})");
	
	p = self.block;
	
	# A and !B and  (  !C  or  !D)
	# A and !B and  (!!!C  or  !D)
	# A and !B and !( !!C and   D)
	# A  -   B  -   (   D and !!C)
	# A  -   B  -   (   D  -   !C)
	
	for s in p.successors:
		# e = set.difference(s.antin, p.avout);
		e = set.difference(s.antin, p.avin);
		if p != start:
			e.difference_update(set.difference(p.antout, p.avkill));
		earliest[(p, s)] = e;
	
	todo = [];
	
	p.phase_counters["earliest"] = phase_counters["earliest"];
	
	for s in p.successors:
		if s.phase_counters["earliest"] < phase_counters["earliest"]:
			todo.append(earliest_phase(s));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















