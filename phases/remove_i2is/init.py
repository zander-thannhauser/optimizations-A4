
from phases.self import phase;

def remove_i2is_phase_init(self, block):
	phase.__init__(self, phase.REMOVE_I2IS);
	self.block = block;


