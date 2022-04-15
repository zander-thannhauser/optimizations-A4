
class printer:
	def __init__(self, filename):
		self.file = open(filename, "w");
		self.identation = 0;
	
	def indent(self):
		self.identation += 1;
	
	def unindent(self):
		self.identation -= 1;
	
	def print(self, string, prefix = "  "):
		print("out: " + prefix + string);
		self.file.write("\t" * self.identation + prefix + string + "\n");
		
	def printf(self, fmt, *args, prefix = "  "):
		self.print(fmt % args, prefix);
	
	def comment(self, fmt, *args):
		self.printf(fmt, *args, prefix = "# ");
	
#	def asm(self, cmd, ins = [], arrow = "", outs = [], prefix = "  "):
#		line = cmd;
#		if ins:
#			line += " " + ", ".join(ins);
#		if arrow:
#			line += " " + arrow;
#		if outs:
#			line += " " + ", ".join(outs);
#		self.print(line, prefix = prefix);
#	
#	def casm(self, cmd, ins = [], arrow = "", outs = []):
#		self.asm(cmd, ins, arrow, outs, prefix = "# ");























