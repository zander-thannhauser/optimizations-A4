
def instruction_str(self):
	out = f"{self.op}(ins = {self.ins}";
	if self.const: out += f", const = {self.const}"
	if self.out:   out += f", out = {self.out}";
	if self.label: out += f", label = {self.label}";
	out += f")"
	return out;

