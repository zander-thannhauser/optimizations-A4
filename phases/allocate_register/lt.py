
def allocate_register_phase_lt(self, other):
	if self.kind < other.kind:
		return True;
	elif self.kind > other.kind:
		return False;
	elif self.liverange.cost > other.liverange.cost:
		return True;
	elif self.liverange.cost < other.liverange.cost:
		return False;
	elif self.liverange.liveid < other.liverange.liveid:
		return True;


