
from debug import *;

from expression_table.self import expression_table;

def parameter_dotout(self, stream, vn, **_):
	# enter("parameter_dotout");
	print(f"""
		"{vn}" [
			shape = diamond
			label = "{self.register}"
			color = "{vn / expression_table.valcounter} 1 1"
		];
	""", file = stream);
	# exit();

