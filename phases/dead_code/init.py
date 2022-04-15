
from phases.self import phase;

def dead_code_phase_init(self, block):
	phase.__init__(self, phase.DEAD_CODE);
	self.block = block;


