
def live_instances_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.block == other.block;

