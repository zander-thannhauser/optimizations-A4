
from expression_table.self import expression_table;

def instruction_newdotout(self, stream, draw_lines = True, constraint = False):
	denominators = expression_table.valcounter;

	name  = f"inst_{self.id}";
	color =  "white";
	
	if self.out is not None:
		if not self.acting_i2i:
			name  = f"{self.out}";
		color = f"{self.out / denominators} 1 1"
	
	label = f"{self.op}"
	
	for vn in self.ins:
		label += f" | <{vn}> %vr{vn}";
		if draw_lines:
			print(f"""
				"{vn}" -> "{name}":"{vn}":n [
					color = "{vn / denominators} 1 1"
					constraint = {"true" if constraint else "false"}
				];
			""", file = stream);
	
	if self.const:
		label += f" | {self.const}";
		
	if self.out is not None:
		label += f" | =\> | %vr{self.out}";
	
	print(f"""
		"{name}" [
			label = "{label}"
			shape = "record"
			fillcolor = "{color}"
			color = "{color}"
			{"style=filled fontcolor=black" if self.is_critical else ""}
		];
	""", file = stream);
	
	if self.acting_i2i:
		print(f"""
			"{name}":s -> "{self.out}" [
				color = "{color}"
			];
		""", file = stream);
	
	return name;











