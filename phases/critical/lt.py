
def critical_phase_lt(self, other):
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	elif self.instruction.id > other.instruction.id:
		return True;


