
def reset_post_dominators_phase_lt(self, other):
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	elif self.block.po < other.block.po:
		return True;


