
from phases.self import phase;

def template_phase_init(self, block):
	phase.__init__(self, phase.template);
	self.block = block;


