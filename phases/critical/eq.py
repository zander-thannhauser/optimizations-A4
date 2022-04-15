
def critical_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.instruction.id == other.instruction.id;



