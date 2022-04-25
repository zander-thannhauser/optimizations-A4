
from phases.self import phase;

def allocate_register_phase_init(self, liverange):
	phase.__init__(self, phase.ALLOCATE_REGISTER);
	self.liverange = liverange;


