
from debug import *;

operator = {
	"add":   "+",
	"fadd": "f+",
	"addI":  "+",
	"comp":  "≶?",
	"cmp_GE": "≥",
	"cmp_GT": ">",
	"cmp_LT": "<",
	"cmp_LE": "≤",
	"cmp_EQ": "=",
	"cmp_NE": "≠",
	"i2f": "i2f",
	"f2i": "f2i",
	"mult": "×",
	"fmult": "f×",
	"multI": "×",
	"mod": "\\%",
	"and": "∧",
	"or":  "∨",
	"sub": "-",
	"not": "¬",
	"rshiftI": ">>",
};

def expression_dotout(self, stream, drawn, et, **_):
	enter("expression_dotout");
	
	dom = et.valcounter;
	
	for subvn in self.ins:
		if subvn not in drawn:
			subex = et.vntoex(subvn);
			subex.dotout(stream, drawn = drawn, et = et);
			drawn.add(subvn);
	
	color = f"{self.valnum / dom} 1 1";
	
	match self.op:
		# those who have one value-number:
		case "not" | "i2f" | "f2i":
			ivn = self.ins[0];
			print(f"""
				"{self.valnum}" [
					shape = square
					label = "{operator[self.op]}"
					color = "{color}"
				];
				"{ivn}":s -> "{self.valnum}":n [color="{ivn / dom} 1 1"];
			""", file = stream);
		
		# those who have one value-number and a constant:
		case "addI" | "multI" | "rshiftI":
			ivn, const = self.ins[0], self.const;
			print(f"""
				"{self.valnum}" [
					shape = box
					label = "{operator[self.op]} ({const})"
					color = "{color}"
				];
				"{ivn}":s -> "{self.valnum}":n [color="{ivn / dom} 1 1"];
			""", file = stream);
		
		# those who have two value-numbers:
		case "comp" | "cmp_GT" | "cmp_LT" | "cmp_LE" | "cmp_GE" | "cmp_EQ" | "cmp_NE" | "mod" | "add" | "fadd" | "sub" | "mult" | "fmult" | "or":
			lvn, rvn = self.ins
			print(f"""
				"{self.valnum}" [
					shape = triangle
					label = "{operator[self.op]}"
					color = "{color}"
				];
				"{lvn}":s -> "{self.valnum}":nw [color="{lvn / dom} 1 1"];
				"{rvn}":s -> "{self.valnum}":ne [color="{rvn / dom} 1 1"];
			""", file = stream);
		
		case _:
			dprint(f"self.op = {self.op}");
			assert(not "TODO");
	
	exit();







