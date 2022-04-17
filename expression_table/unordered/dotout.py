
from debug import *;

operator = {
	"and":  "∀",
};

def unordered_dotout(self, stream, drawn, et, **_):
	enter("unordered_dotout");
	
	dom = et.valcounter;
	
	for subvn in self.ins:
		if subvn not in drawn:
			subex = expression_table.vntoex(subvn);
			subex.dotout(stream, subvn, drawn = drawn, et = et);
			drawn.add(subvn);
		print(f"""
			"{subvn}":s -> "{self.valnum}" [
				color = "{subvn / dom} 1 1"
			];
		""", file = stream);
	
	color = f"{self.valnum / dom} 1 1";
	
	print(f"""
		"{self.valnum}" [
			shape = invtrapezium
			label = "{operator[self.op]}"
			color = "{color}"
		];
	""", file = stream);
		
	exit();




