
from debug import *;

from phases.self import phase;

def inheritance_phase_dotout(self, all_dots, all_blocks, **_):
	
	enter("inheritance_phase_dotout()");
	
	filename = f"dot/{phase.frame_counter}-inheritance.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	print("""
digraph mygraph {

	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		ins = " | ".join(f"<in_{r[1:]}> {r}" for r in block.ins);
		
		label = f"rpo = {block.rpo}";
		
		outs = " | ".join(f"<out_{r[1:]}> {r}" for r in block.outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			"{id(block)}" [
				shape=record
				label="{label}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"\"{id(block)}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
		if block.given is not None:
			for register, feeders in block.given.items():
				for feeder in feeders:
					print(f"""
						"{id(feeder)}":"out_{register[1:]}":s ->
						"{id(block)}": "in_{register[1:]}":n [
							style = dashed
							constraint = false
							color = "{feeder.hue} 1 1"
						]
					""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















