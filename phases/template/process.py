
from debug import *;

from phases.template.self import template_phase;

def template_phase_process(self, phase_counters, **_):
	enter(f"template.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	assert(not "TODO");
	
	block.phase_counters["template"] = phase_counters["template"]
	
	for child in block.successors:
		if child.phase_counters["template"] < phase_counters["template"]:
			todo.append(template_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















