
from debug import *;

from phases.self import phase;

def earliest_phase_dotout(self, all_blocks, earliest, **_):
	
	enter("earliest_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-earliest.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [fontname="Courier New" color=white fontcolor=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for p in all_blocks:
		bid = id(p);
		
		avout = "|".join(str(a) for a in p.avout);
		antin = "|".join(str(a) for a in p.antin);
		kill = "|".join(str(a) for a in p.avkill);
		antout = "|".join(str(a) for a in p.antout);
		
		label = ("{{antin:|%s} | "
				+ "{avout:|%s} | "
				+ "{kill:|%s} | "
				+ "{antout:|%s}}") \
			% (antin, avout, kill, antout);
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{p.hue} 1 1"
				shape=record
				{"style=bold" if p == self.block else ""}
			];
		""", file = stream);
		
		for s in p.successors:
			print(f"""
				"{bid}" -> "{id(s)}" [
					style = bold
					label = "earliest: {sorted(earliest.get((p, s), []))}"
				]
			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















