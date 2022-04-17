
def multiplicity_hash(self):
	return hash(("multiplicity", self.op, *sorted(self.ins)));


