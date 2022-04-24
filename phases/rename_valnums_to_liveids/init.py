
from phases.self import phase;

def rename_valnums_to_liveids_phase_init(self, block):
	phase.__init__(self, phase.RENAME_VALNUMS_TO_LIVEIDS);
	self.block = block;


