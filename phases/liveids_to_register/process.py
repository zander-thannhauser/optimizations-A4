
from debug import *;

from phases.liveids_to_register.self import liveids_to_register_phase;

def liveids_to_register_phase_process(self, all_liveranges, **_):
	enter(f"liveids_to_register.process(self.liverange = {self.liverange})");
	
	lr = self.liverange;
	
	dprint(f"lr = {lr}")
	
	if lr in all_liveranges:
		for d in lr.definers:
			assert(lr.liveid == d.out);
			d.out = f"%vr{lr.register}"
		for u in lr.users:
			assert(lr.liveid in u.ins);
			u.ins[u.ins.index(lr.liveid)] = f"%vr{lr.register}";
	else:
		assert(not "TODO");
	
	exit(f"return");
	return [];






















