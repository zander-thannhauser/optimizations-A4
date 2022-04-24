
from phases.self import phase;

def build_interference_phase_init(self, block):
	phase.__init__(self, phase.BUILD_INTERFERENCE);
	self.block = block;


