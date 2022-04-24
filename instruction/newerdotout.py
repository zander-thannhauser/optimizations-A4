
def instruction_newerdotout(self, stream, denominator):

	name  = f"{id(self)}";
	color =  "white";
	
	if self.out is not None:
		color = f"{self.out / denominator} 1 1"
	
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
			{"style=filled fontcolor=black" if self.is_critical else ""}
		];
	""", file = stream);
	
	return name;











