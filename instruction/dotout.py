
from expression_table.self import expression_table;

from .self import instruction;

def instruction_dotout(self, stream, block):
	name = f"{id(block)}_{self.id}";
	hue = self.id / instruction.counter;
	label = self.op;
	for i in self.ins:
		label += f"| {i}";
	if self.const is not None:
		label += f"| {self.const}";
	if self.out is not None:
		label += f"| =\\> | {self.out}";
	print(f"""
		"{name}" [
			label = "{label}"
			shape = "record"
			color = "{hue} 1 1"
		];
	""", file = stream);
	return name;


