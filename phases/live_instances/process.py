
from debug import *;

from liverange.self import liverange;

from phases.live_instances.self import live_instances_phase;

def live_instances_phase_process(self, start, parameters, all_liveranges, defineset_to_liverange, **_):
	enter(f"live_instances.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	liveout = dict();
	
	if block == start:
		for p in parameters:
			new = liverange(p.liveid);
			all_liveranges.add(new);
			liveout[p.liveid] = new;
			p.liverange = new;
	else:
		for parent in block.predecessors:
			if parent.liveout is not None:
				for liveid, instance in parent.liveout.items():
					if liveid not in liveout:
						liveout[liveid] = instance;
					else:
						before = liveout[liveid];
						dprint(f"before = {before}")
						dprint(f"instance = {instance}")
						assert(liveout[liveid] == instance);
	
	for inst in block.newer_instructions:
		dprint(f"inst = {inst}");
		
		for i in inst.ins:
			assert(i in liveout);
			lr = liveout[i];
			dprint(f"lr = {lr}")
			lr.users.add(inst);
			inst.live_use_list[i] = lr;
		
		if inst.out is not None:
			define_set = tuple(sorted(inst.define_set));
			
			# dprint(f"define_set = {[str(d) for d in define_set]}")
			
			if define_set in defineset_to_liverange:
				lr = defineset_to_liverange[define_set];
				dprint(f"recalling live range ({lr})");
			else:
				lr = liverange(inst.out);
				defineset_to_liverange[define_set] = lr;
				all_liveranges.add(lr);
				dprint(f"created new live range ({lr})");
			
			lr.definers.add(inst);
			liveout[inst.out] = lr;
	
	if block.newer_jump:
		inst = block.newer_jump;
		
		dprint(f"jump = {inst}");
		
		for i in inst.ins:
			assert(i in liveout);
			lr = liveout[i];
			dprint(f"lr = {lr}")
			lr.users.add(inst);
			inst.live_use_list[i] = lr;
	
	if len(block.successors):
		needed = set.union(*(s.live_ins for s in block.successors))
	else:
		needed = set();
	
	dprint(f"needed = {needed}");
	dprint(f"liveout = {liveout}");
	
	for livein in list(liveout.keys()):
		if livein not in needed and livein not in [0, 1, 2, 3]:
			del liveout[livein];
	
	dprint(f"liveout = {liveout}");
	
	if block.liveout != liveout:
		for child in block.successors:
			todo.append(live_instances_phase(child));
		block.liveout = liveout;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















