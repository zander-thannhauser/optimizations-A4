
from phases.self import phase;

def earliest_phase_init(self, block):
	phase.__init__(self, phase.EARLIEST);
	self.block = block;


