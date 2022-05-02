
from debug import *;

from phases.self import phase;

def lost_parent_phase_dotout(self, all_blocks, all_dots, **_):
	
	enter("lost_parent_phase_dotout()");
	
	filename = f"dot/{phase.frame_counter}-lost-parent.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		print(f"""
			"{bid}" [
				label="rpo = {block.rpo}"
				color="{block.hue} 1 1"
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















