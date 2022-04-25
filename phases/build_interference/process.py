
from debug import *;

from phases.calculate_cost.self import calculate_cost_phase;
from phases.build_interference.self import build_interference_phase;

def build_interference_phase_process(self, all_blocks, all_liveranges, vnsets_to_liveid, interference, phase_counters, **_):
	enter(f"build_interference.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	liveout = block.liveout;
	
	if block.newer_jump:
		inst = block.newer_jump;
		
		dprint(f"inst = {inst}");
		
		for i in inst.ins:
			liveout[i] = inst.live_use_list[i];
		
		self.subdotout(all_blocks, all_liveranges, vnsets_to_liveid, interference, liveout, inst);
	
	todo = [];
	
	for inst in block.newer_instructions[::-1]:
		dprint(f"inst = {inst}");
		
		if inst.out is not None:
			assert(inst.out in liveout);
			# remove instance from mapping
			bye = liveout.pop(inst.out);
			
			# mark this instance as iterfering with
			# all other instances in current mapping
			for other in liveout.values():
				# just for graphviz:
				other.interference_points.add(inst);
				other.interference_with[inst] = bye;
				interference.add((min(bye, other), max(bye, other)));
			
			todo.append(calculate_cost_phase(bye));
			
		for i in inst.ins:
			liveout[i] = inst.live_use_list[i];
		
		self.subdotout(all_blocks, all_liveranges, vnsets_to_liveid, interference, liveout, inst);
	
	block.phase_counters["build_interference"] = phase_counters["build_interference"]
	
	for parent in block.predecessors:
		if parent.phase_counters["build_interference"] < phase_counters["build_interference"]:
			todo.append(build_interference_phase(parent));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















