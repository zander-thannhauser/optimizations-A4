
from phases.self import phase;

def in_out_phase_init(self, block):
	phase.__init__(self, phase.IN_OUT);
	self.block = block;


