
import math;

def liverange_dotout(self, stream, denominator = None):
	
	label = f"%lr{self.liveid}"
	
	o, c = '{', '}';
	
	if denominator is not None:
		self.hue = self.liveid / denominator;
	
	color = f"{self.hue} 1 1";
	
	last = None;
	
	all = set.union(self.definers, self.users, self.interference_points);

	if self.cost is None:
		line_attributes = ""
	elif self.cost == float('inf'):
		line_attributes = """
			color = "white:black:white";
		"""
	elif self.cost < 1:
		line_attributes = """
			style = dashed;
		"""
	else:
		line_attributes = f"""
			penwidth = {math.log(self.cost) + 1}
		"""
	
	fillcolor = "black";
	fontcolor = "white"
	
	if self.register is not None:
		fillcolor = f"{self.hue} 1 1";
		fontcolor = "black"
	
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
			if denominator is not None:
				other.hue = other.liveid / denominator;
			thiscolor = f"{other.hue} 1 1";
			other = "width = 0.1";
			shape = "point";
		
		print(f"""
			"{name}" [
				shape = "{shape}"
				label = "{label}"
				color = "{thiscolor}"
				fillcolor = "{fillcolor}"
				style = filled
				fontcolor = {fontcolor}
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
					{line_attributes}
				];
			""", file = stream);
			
		last = name;
	
	

