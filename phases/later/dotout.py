
from debug import *;

from phases.self import phase;

def later_phase_dotout(self, all_blocks, earliest, later, insert, **_):
	
	enter("later_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-later.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [fontname="Courier New" color=white fontcolor=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for p in all_blocks:
		bid = id(p);
		
		antlocal = "|".join(str(a) for a in p.antloc);
		
		laterin = "None" if p.laterin is None else "|".join(str(a) for a in p.laterin);
		
		delete = "|".join(str(a) for a in p.delete);
		
		label = ("{{antlocal:|%s} | "
		        +" {laterin:|%s}| "
		        +" {delete:|%s}}") \
			% (antlocal, laterin, delete);
		
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
					label = "earliest: {sorted(earliest.get((p, s), []))}\\nlater: {sorted(later.get((p, s), []))}\\ninsert: {sorted(insert.get((p, s), []))}"
				]
			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















