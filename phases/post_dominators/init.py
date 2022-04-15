
from phases.self import phase;

def post_dominators_phase_init(self, block):
	phase.__init__(self, phase.POST_DOMINATORS);
	self.block = block;


