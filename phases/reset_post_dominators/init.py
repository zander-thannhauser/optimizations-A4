
from phases.self import phase;

def reset_post_dominators_phase_init(self, block):
	phase.__init__(self, phase.RESET_POST_DOMINATORS);
	self.block = block;
