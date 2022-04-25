
def liverange_dotout(self, stream, denominator):
	
	label = f"%lr{self.liveid}"
	
	o, c = '{', '}';
	
	color = f"{self.liveid / denominator} 1 1";
	
	last = None;
	
	all = set.union(self.definers, self.users, self.interference_points);
	
	for i, inst in enumerate(sorted(all)):
		name = f"{id(self)}_{id(inst)}";
		
		other = "";
		
		if inst in self.definers:
			shape = "doublecircle";
			thiscolor = color;
		elif inst in self.users:
			shape = "circle";
			thiscolor = color;
		else:
			other = self.interference_with[inst];
			thiscolor = f"{other.liveid / denominator} 1 1";
			other = "width = 0.1";
			shape = "point";
		
		print(f"""
			"{name}" [
				shape = "{shape}"
				label = "{label}"
				color = "{thiscolor}"
				{other}
			];
			
			{o}
				rank = same;
				"{id(inst)}"; "{name}";
			{c}
		""", file = stream);
		
		if last is not None:
			print(f"""
				"{last}" -> "{name}" [
					dir = none
				];
			""", file = stream);
			
		last = name;
	
	

