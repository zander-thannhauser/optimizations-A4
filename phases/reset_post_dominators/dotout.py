
from debug import *;

from phases.self import phase;

def reset_post_dominators_phase_dotout(self, all_blocks, **_):
	
	enter("reset_post_dominators_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}.txt", "w");
	
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
				label="po = {block.po}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for s in block.successors:
			print(f"\"{bid}\":s -> \"{id(s)}\":n [style=bold]", file = stream);
		
		for d in block.post_dominators:
			print(f"\"{bid}\" -> \"{id(d)}\" [color=\"{d.hue} 1 1\"]", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















