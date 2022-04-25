
def liverange_str(self):
	x = f"liverange(liveid = {self.liveid}, instance = {self.instance_id}"
	if self.cost is not None:
		x += f", cost = {self.cost}"
	return x + ")";


