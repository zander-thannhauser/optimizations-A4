
from debug import dprint;

def multiplicity_eq(self, other):
	# dprint(f"multiplicity_eq: {self.ins} vs. {other.ins}")
	return True \
		and self.op == other.op \
		and self.ins == other.ins;


