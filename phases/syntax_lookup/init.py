
from phases.self import phase;

def syntax_lookup_phase_init(self, block):
	phase.__init__(self, phase.SYNTAX_LOOKUP);
	self.block = block;


