
from debug import *;

from phases.self import phase;

def in_out_phase_dotout(self, all_blocks, **_):
	
	enter("in_out_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		ins = "None" if block.ins is None else " | ".join(block.ins);
		label = f"po = {block.po}";
		outs = " | ".join(block.outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"\"{bid}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















