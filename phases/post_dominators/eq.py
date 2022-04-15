
def post_dominators_phase_eq(self, other):
	return True \
		and self.kind == other.kind \
		and self.block.po == other.block.po;



