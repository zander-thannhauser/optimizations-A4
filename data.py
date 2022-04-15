
def process_data(t, p):
	if (t.token == ".data"):
		p.printf(".data", prefix = "");
		p.indent();
		while True:
			token = next(t);
			if token == ".string":
				label = next(t);
				assert(next(t) == ',');
				literal = next(t);
				p.printf("%8s %16s, %s", ".string", label, literal);
			elif token == ".float":
				label = next(t);
				assert(next(t) == ',');
				literal = next(t);
				p.printf("%8s %16s, %s", ".float", label, literal);
			elif token == ".global":
				label = next(t);
				assert(next(t) == ',');
				align = next(t);
				assert(next(t) == ',');
				size = next(t);
				p.printf("%8s %16s, %s, %s", ".global", label, align, size);
			else:
				break;
		p.unindent();
