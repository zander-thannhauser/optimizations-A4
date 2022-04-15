
from debug import *;

from expression_table.self import expression_table;

def unknown_dotout(self, stream, vn, **_):
	enter("unknown_dotout");
	assert(self.instruction);
	print(f"""
		"{vn}" [
			shape = invhouse
			label = "{self.instruction.op}"
			color = "{vn / expression_table.valcounter} 1 1"
			fillcolor = "{vn / expression_table.valcounter} 1 1"
		];
	""", file = stream);
	
	for subvn in self.instruction.ins:
		print(f"""
			"{subvn}" -> "{vn}";
		""", file = stream);
	
	exit();

