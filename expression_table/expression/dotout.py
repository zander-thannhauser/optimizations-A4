
from debug import *;

from expression_table.self import expression_table;

operator = {
	"add":  "+",
	"addI": "+",
	"comp": "≶?",
	"cmp_GE": "≥",
	"cmp_GT": ">",
	"cmp_LT": "<",
	"cmp_LE": "≤",
	"multI": "×",
};

def expression_dotout(self, stream, vn, done, expression_table):
	enter("expression_dotout");
	
	dom = expression_table.valcounter;
	
	for subvn in self.ins:
		if subvn not in done:
			subex = expression_table.vntoex(subvn);
			subex.dotout(stream, subvn, done = done, expression_table = expression_table);
			done.add(subvn);
	
	color = f"{vn / dom} 1 1";
	
	match self.op:
		# those who have one value-number and a constant:
		case "addI" | "multI":
			ivn, const = self.ins[0], self.const;
			print(f"""
				"{vn}" [
					shape = box
					label = "{operator[self.op]} ({const})"
					color = "{color}"
				];
				"{ivn}":s -> "{vn}":w [color="{ivn / dom} 1 1"];
			""", file = stream);
		
		# those who have two value-numbers:
		case "add" | "comp" | "cmp_GT" | "cmp_LT" | "cmp_LE" | "cmp_GE":
			lvn, rvn = self.ins
			print(f"""
				"{vn}" [
					shape = triangle
					label = "{operator[self.op]}"
					color = "{color}"
				];
				"{lvn}":s -> "{vn}":nw [color="{lvn / dom} 1 1"];
				"{rvn}":s -> "{vn}":ne [color="{rvn / dom} 1 1"];
			""", file = stream);
		
		case _:
			dprint(f"self.op = {self.op}");
			assert(not "TODO");
	
	exit();












