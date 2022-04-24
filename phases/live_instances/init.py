
from phases.self import phase;

def live_instances_phase_init(self, block):
	phase.__init__(self, phase.LIVE_INSTANCES);
	self.block = block;


