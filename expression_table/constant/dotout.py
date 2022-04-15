
from debug import *;

from expression_table.self import expression_table;

def constant_dotout(self, stream, vn, **_):
	enter("constant_dotout");
	print(f"""
		"{vn}" [
			shape = circle
			label = "{self.value}"
			color = "{vn / expression_table.valcounter} 1 1"
			fillcolor = "{vn / expression_table.valcounter} 1 1"
		];
	""", file = stream);
	exit();

