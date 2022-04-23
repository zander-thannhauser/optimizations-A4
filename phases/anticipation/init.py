
from phases.self import phase;

def anticipation_phase_init(self, block):
	phase.__init__(self, phase.ANTICIPATION);
	self.block = block;


