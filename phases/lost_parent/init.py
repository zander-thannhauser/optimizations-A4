
from phases.self import phase;

def lost_parent_phase_init(self, block):
	phase.__init__(self, phase.LOST_PARENT);
	self.block = block;


