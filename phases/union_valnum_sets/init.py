
from phases.self import phase;

def union_valnum_sets_phase_init(self, block):
	phase.__init__(self, phase.UNION_VALNUM_SETS);
	self.block = block;


