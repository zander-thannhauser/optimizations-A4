
from phases.self import phase;

def loop_depth_phase_init(self, block):
	phase.__init__(self, phase.LOOP_DEPTH);
	self.block = block;


