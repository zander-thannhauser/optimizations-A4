
def expression_eq(self, other):
	return True \
		and self.op == other.op \
		and self.ins == other.ins \
		and self.const == other.const;


