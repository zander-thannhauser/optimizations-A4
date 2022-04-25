
def liveids_to_register_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.liverange == other.liverange;

