
from phases.self import phase;

def reset_in_out_phase_init(self, block):
	phase.__init__(self, phase.RESET_IN_OUT);
	self.block = block;


