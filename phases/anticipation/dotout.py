
from debug import *;

from phases.self import phase;

def anticipation_phase_dotout(self, all_blocks, **_):
	
	enter("anticipation_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-anticipation.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		antoutgoing = "None" if block.antin is None else "|".join(str(a) for a in block.antin);
		antkilled = "|".join(str(a) for a in block.antkill);
		antlocal = "|".join(str(a) for a in block.antloc);
		antincoming = "|".join(str(a) for a in block.antout);
		
		label = ("{{antin:|%s} | {antkill:|%s} | {antloc:|%s} | {antout:|%s}}") \
			% (antoutgoing, antkilled, antlocal, antincoming);
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{block.hue} 1 1"
				shape=record
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for s in block.successors:
			print(f"""
				"{bid}" -> "{id(s)}" [
					style = bold
				]
			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















