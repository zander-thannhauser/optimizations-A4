
def liverange_dotout(self, stream, denominator):
	
	name = id(self);
	
#	label = f"Φ"
	label = f"#{self.liveid}"
#	label = f"{self.liveid}, {self.instance_id}"
	
	hue = self.liveid / denominator;
	
	print(f"""
		"{name}" [
			shape = circle
			label = "{label}"
			color = "{hue} 1 1"
		];
	""", file = stream);
	
	for definer in self.definers:
		print(f"""
			"{id(definer)}" -> "{name}" [
				color = "{hue} 1 1"
			];
		""", file = stream);
		
	for user in self.users:
		print(f"""
			"{name}" -> "{id(user)}" [
				color = "{hue} 1 1"
			];
		""", file = stream);
	
	

