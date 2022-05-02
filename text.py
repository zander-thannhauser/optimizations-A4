
from frame import process_frame;

def process_text(t, p, num_registers):
	if (t.token == ".text"):
		p.printf(".text", prefix = "");
		p.indent();
		
		all_dots = open("dot/all-dots.mk", "w");
		
		t.next();
		while (t.token == ".frame"):
			process_frame(t, p, all_dots, num_registers);
		
		all_mk.close();
		
		p.unindent();
	
























