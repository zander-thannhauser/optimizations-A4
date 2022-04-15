
from phases.self import phase;

def phi_phase_init(self, block):
	phase.__init__(self, phase.PHI);
	self.block = block;


