
from phases.self import phase;

def available_phase_init(self, block):
	phase.__init__(self, phase.AVAILABLE);
	self.block = block;


