
def unordered_hash(self):
	return hash(("unordered", self.op, *sorted(self.ins)));


