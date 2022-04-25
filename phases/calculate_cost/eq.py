
def calculate_cost_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.liverange == other.liverange;

