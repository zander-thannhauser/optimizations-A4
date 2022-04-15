
from phases.self import phase;

def optimize_phase_init(self, block):
	phase.__init__(self, phase.OPTIMIZE);
	self.block = block;


