
from debug import *;

from instruction.self import instruction;

from phases.live_in_out.self import live_in_out_phase;
from phases.live_instances.self import live_instances_phase;
from phases.spill_liverange.self import spill_liverange_phase;
from phases.live_inheritance.self import live_inheritance_phase;
from phases.build_interference.self import build_interference_phase;

def spill_liverange_phase_process(self, frame, start, end, all_blocks, all_liveranges, vnsets_to_liveid, defineset_to_liverange, interference, phase_counters, **_):
	enter(f"spill_liverange.process(self.liverange = {self.liverange})");
	
	lr = self.liverange;
	
	todo = [];
	
	denominator = vnsets_to_liveid["next"]
	
	if lr in all_liveranges:
		
		if len(lr.definers) == 1 and (loadI := list(lr.definers)[0]).op == "loadI":
			
			block = loadI.block;
			block.newer_instructions.remove(loadI);
			
			for inst in lr.users:
				block = inst.block;
				new = instruction("loadI", [], const = loadI.const, out = lr.liveid);
				new.hue = loadI.hue;
				new.block = block;
				new.is_critical = True;
				
				if inst in block.newer_instructions:
					index = block.newer_instructions.index(inst);
					block.newer_instructions.insert(index, new);
				else:
					assert(block.newer_jump == inst);
					block.newer_instructions.append(new);
			
		else:
			offset = frame["framesize"];
			
			for inst in lr.definers:
				block = inst.block;
				index = block.newer_instructions.index(inst);
				storeAI = instruction("storeAI", [lr.liveid, 0], const = -offset);
				storeAI.block = block;
				storeAI.is_critical = True;
				block.newer_instructions.insert(index + 1, storeAI);
				
			for inst in lr.users:
				block = inst.block;
				loadAI = instruction("loadAI", [0], const = -offset, out = lr.liveid);
				loadAI.hue = lr.liveid / denominator;
				loadAI.block = block;
				loadAI.is_critical = True;
				
				if inst in block.newer_instructions:
					index = block.newer_instructions.index(inst);
					block.newer_instructions.insert(index, loadAI);
				else:
					assert(block.newer_jump == inst);
					block.newer_instructions.append(loadAI);
			
			frame["framesize"] += 4;
		
		# reset shared values:
		defineset_to_liverange.clear();
		
		all_liveranges.clear();
		
		interference.clear();
		
		phase_counters["build_interference"] += 1;
		
		for block in all_blocks:
			block.live_ins = None;
			block.live_outs = dict();
			block.live_given = None;
			block.liveout = None;
		
		todo = [
			live_in_out_phase(end), # bottom-up:
			live_inheritance_phase(start), # top-down:
			live_instances_phase(start), # top-down*:
			build_interference_phase(end), # bottom-up:
		];
		
	else:
		dprint(f"old spill, ignoring...")
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















