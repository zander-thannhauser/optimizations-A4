
from phases.self import phase;

def calculate_cost_phase_init(self, liverange):
	phase.__init__(self, phase.CALCULATE_COST);
	self.liverange = liverange;


