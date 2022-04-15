
from frame import process_frame;

def process_text(t, p):
	if (t.token == ".text"):
		p.printf(".text", prefix = "");
		p.indent();
		
		t.next();
		while (t.token == ".frame"):
			process_frame(t, p);
		
		p.unindent();
	
























