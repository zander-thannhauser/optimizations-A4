
from debug import *;

from phases.self import phase;

def inheritance_phase_dotout(self, all_blocks, **_):
	
	enter("inheritance_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		ins = " | ".join(f"<in_{r[1:]}> {r}" for r in block.ins);
		
		label = f"po = {block.po}";
		
		outs = " | ".join(f"<out_{r[1:]}> {r}" for r in block.outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			"{id(block)}" [
				label="{label}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"\"{id(block)}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
		for register, feeders in block.given.items():
			for feeder in feeders:
				print(f"""
					"{id(feeder)}":"out_{register[1:]}":s ->
					"{id(block)}": "in_{register[1:]}":n
					 [style=dashed color="{feeder.hue} 1 1"]
				""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















