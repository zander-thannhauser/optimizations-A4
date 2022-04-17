
from debug import *;

operator = {
	"sum":  "∑",
	"product": "∏",
};

def multiplicity_dotout(self, stream, drawn, et, **_):
	enter("multiplicity_dotout");
	
	dom = et.valcounter;
	
	for subvn, multiplicity in self.ins:
		if subvn not in drawn:
			subex = et.vntoex(subvn);
			subex.dotout(stream, drawn = drawn, et = et);
			drawn.add(subvn);
		print(f"""
			"{subvn}":s -> "{self.valnum}":"{subvn}":n [
				color = "{subvn / dom} 1 1"
			];
		""", file = stream);
	
	color = f"{self.valnum / dom} 1 1";
	
	label = "{{%s} | %s}" % \
		("|".join(f"<{s}> {m}" for s, m in self.ins), operator[self.op])
	
	print(f"""
		"{self.valnum}" [
			shape = record
			label = "{label}"
			color = "{color}"
		];
	""", file = stream);
		
	exit();
















