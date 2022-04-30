
from phases.self import phase;

def later_phase_init(self, block):
	phase.__init__(self, phase.LATER);
	self.block = block;


