
from phases.self import phase;

def insert_delete_phase_init(self, block):
	phase.__init__(self, phase.INSERT_DELETE);
	self.block = block;


