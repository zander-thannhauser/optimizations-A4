
def anticipation_phase_lt(self, other):
	print(f"self.block.label, other.block.label = {self.block.label, other.block.label}")
	print(f"self.block.po, other.block.po = {self.block.po, other.block.po}")
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	elif self.block.po < other.block.po:
		return True;


