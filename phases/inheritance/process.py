
from debug import *;

from phases.inheritance.self import inheritance_phase;

def inheritance_phase_process(self, all_blocks, phase_counters, **_):
	enter(f"inheritance_phase.process(block.po = {self.block.po})");
	
	block = self.block;
	
	giving = block.given.copy();
	
	for reg in block.outs:
		giving[reg] = set([block]);
	
	dprint(f"giving = {giving}");
	
	todo = [];
	
	block.phase_counters["inheritance"] = phase_counters["inheritance"];
	
	for successor in block.successors:
		changed = False;
		
		for register in successor.ins:
			assert(register in giving);
			
			sources = giving[register];
			
			subgiven = successor.given.setdefault(register, set());
			
			if not sources.issubset(subgiven):
				changed = True;
				subgiven.update(sources);
		
		dprint(f"{block.po} onto {successor.po}: changed = {changed}");
		
		if changed or successor.phase_counters["inheritance"] < phase_counters["inheritance"]:
			todo.append(inheritance_phase(successor));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















