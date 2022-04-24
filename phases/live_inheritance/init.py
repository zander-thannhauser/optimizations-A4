
from phases.self import phase;

def live_inheritance_phase_init(self, block):
	phase.__init__(self, phase.LIVE_INHERITANCE);
	self.block = block;


