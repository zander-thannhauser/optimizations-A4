
from debug import *;

from phases.later.self import later_phase;

def later_phase_process(self, earliest, later, insert, **_):
	enter(f"later_phase_process(block.rpo = {self.block.rpo})");
	
	b = self.block;
	
	laterin = set();
	
	if len(b.predecessors):
		for p in b.predecessors:
			if p.laterin is not None:
				later[(p, b)] = set.union(set.difference(p.laterin, p.antloc), earliest[(p, b)]);
	
		laterin = set.intersection(*(later[(p, b)] for p in b.predecessors if p.laterin is not None));
	
	dprint(f"laterin = {laterin}")
	
	for p in b.predecessors:
		if p.laterin is not None:
			insert[(p, b)] = set.difference(later[(p, b)], laterin);
	
	b.delete = set.difference(b.antloc, laterin);
	
	todo = [];
	
	if b.laterin != laterin:
		for s in b.successors:
			todo.append(later_phase(s));
		b.laterin = laterin;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















