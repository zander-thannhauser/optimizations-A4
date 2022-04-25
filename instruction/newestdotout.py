
from debug import *;

def instruction_newestdotout(self, stream, denominator = None):

	name  = f"{id(self)}";
	color =  "white";
	
	if self.out is not None:
		if denominator is not None:
			match self.out:
				case str(): self.hue = int(self.out[3:]) / denominator;
				case int(): self.hue = self.out / denominator;
				case _: assert(not "TODO");
			
		color = f"{self.hue} 1 1"
	
	label = f"{self.op}"
	
	for vr in self.ins:
		label += f" | {vr}";
	
	if self.const is not None:
		label += f" | {self.const}";
		
	if self.out is not None:
		label += f" | =\> | {self.out}";
	
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











