
from phases.self import phase;

def critical_phase_init(self, instruction):
	phase.__init__(self, phase.CRITICAL);
	self.instruction = instruction;


