
from phases.self import phase;

def liveids_to_register_phase_init(self, liverange):
	phase.__init__(self, phase.LIVEIDS_TO_REGISTER);
	self.liverange = liverange;


