
def rename_valnums_to_liveids_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.block == other.block;

