
def instruction_str(self):
	out = f"{self.op}(vr_ins = {self.vr_ins}";
	if self.const: out += f", const = {self.const}"
	if self.vr_out:out += f", vr_out = {self.vr_out}";
	if self.label: out += f", label = {self.label}";
	out += f")"
	return out;

