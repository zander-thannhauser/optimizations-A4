
def liverange_newdotout(self, stream, denominator):
	
	name = id(self);
	
#	label = f"Φ"
	label = f"%lr{self.liveid}"
#	label = f"{self.liveid}, {self.instance_id}"
	
	hue = self.liveid / denominator;
	
	print(f"""
		"{name}" [
			shape = circle
			label = "{label}"
			color = "{hue} 1 1"
		];
	""", file = stream);
	
	if len(self.definers):
		highest = min(self.definers, key = lambda i: i.id);
		
		print("{" + f"""
			rank = same
			"{name}"; "{id(highest)}";
		""" + "}", file = stream);
	
	
