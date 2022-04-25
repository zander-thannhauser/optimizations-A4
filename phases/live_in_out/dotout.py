
from debug import *;

from phases.self import phase;

def live_in_out_phase_dotout(self, all_blocks, **_):
	
	enter("live_in_out_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-liveinout.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		ins = "None" if block.live_ins is None else " | ".join(f"%lr{x}" for x in block.live_ins);
		label = f"rpo = {block.rpo}";
		outs = " | ".join(f"%lr{x}" for x in block.live_outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"""
				"{bid}":s -> "{id(c)}":n [
					style = bold
				]
			""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















