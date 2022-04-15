
from expression_table.self import expression_table;

def phi_dotout(self, stream, valnum, **_):
	print(f"""
		"{valnum}" [
			label = "𝜙"
			shape = doublecircle
			color = "{valnum / expression_table.valcounter} 1 1"
			fillcolor = "{valnum / expression_table.valcounter} 1 1"
			{"style=filled fontcolor=black" if self.is_critical else ""}
		];
	""", file = stream);

