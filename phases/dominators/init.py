
from phases.self import phase;

def dominators_phase_init(self, block):
	phase.__init__(self, phase.DOMINATORS);
	self.block = block;


