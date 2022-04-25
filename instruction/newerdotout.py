
def instruction_newerdotout(self, stream, denominator = None):

	name  = f"{id(self)}";
	color =  "white";
	
	if self.out is not None:
		if denominator is not None:
			self.hue = self.out / denominator;
		color = f"{self.hue} 1 1"
	
	label = f"{self.op}"
	
	for lrid in self.ins:
		label += f" | <{lrid}> %lr{lrid}";
	
	if self.const is not None:
		label += f" | {self.const}";
		
	if self.out is not None:
		label += f" | =\> | %lr{self.out}";
	
	print(f"""
		"{name}" [
			label = "{label}"
			shape = "record"
			fillcolor = "{color}"
			color = "{color}"
			{"style = filled fontcolor=black" if self.is_critical else ""}
		];
	""", file = stream);
	
	return name;











