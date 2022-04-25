
from phases.self import phase;

def spill_liverange_phase_init(self, liverange):
	phase.__init__(self, phase.SPILL_LIVERANGE);
	self.liverange = liverange;


