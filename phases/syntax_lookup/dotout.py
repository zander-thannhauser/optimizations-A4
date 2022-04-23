
from debug import *;

from phases.self import phase;

def syntax_lookup_phase_dotout(self, all_blocks, **_):
	
	enter("syntax_lookup_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-syntax_lookup.txt", "w");
	
	print("""
digraph mygraph {

	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		print(f"""
			"{bid}" [
				label = "rpo = {block.rpo}"
				color = "{block.hue} 1 1"
				shape = record
				{"style = bold" if block == self.block else ""}
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















