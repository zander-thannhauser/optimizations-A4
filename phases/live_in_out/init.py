
from phases.self import phase;

def live_in_out_phase_init(self, block):
	phase.__init__(self, phase.LIVE_IN_OUT);
	self.block = block;


