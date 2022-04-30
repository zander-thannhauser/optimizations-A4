
def available_phase_lt(self, other):
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	elif self.block.rpo < other.block.rpo:
		return True;


