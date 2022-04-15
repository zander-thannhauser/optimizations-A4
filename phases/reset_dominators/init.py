
from phases.self import phase;

def reset_dominators_phase_init(self, block):
	phase.__init__(self, phase.RESET_DOMINATORS);
	self.block = block;


