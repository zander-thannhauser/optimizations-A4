
from phases.self import phase;

def reset_dominators_phase_init(self, block, target = None):
	phase.__init__(self, phase.RESET_DOMINATORS);
	self.block = block;
	self.target = target;


