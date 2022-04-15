
depth = 0;

def indent():
	global depth;
	depth += 1;

def unindent():
	global depth;
	depth -= 1;

def dprint(string):
	global depth;
	print(" " * depth + str(string));

def enter(string):
	dprint(string + ":");
	indent();

def exit(string = "return;"):
	dprint(string);
	unindent();

def dpv():
	assert(not "TODO");

