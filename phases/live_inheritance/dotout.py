
from debug import *;

from phases.self import phase;

def live_inheritance_phase_dotout(self, all_blocks, **_):
	
	enter("live_inheritance_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-live_inheritance.dot", "w");
	
	assert(not "TODO");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	print("""
digraph mygraph {

	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		ins = " | ".join(f"<in_{r}> {r}" for r in block.live_ins);
		
		label = f"rpo = {block.rpo}";
		
		outs = " | ".join(f"<out_{r}> {r}" for r in block.live_outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		print(f"""
			"{id(block)}" [
				shape = record
				label = "{label}"
				color = "{block.hue} 1 1"
				{"style = bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"""
				"{id(block)}":s -> "{id(c)}":n [
					style = bold
				]
			""", file = stream);
		
		if block.live_given is not None:
			for register, feeders in block.live_given.items():
				for feeder in feeders:
					feeder_block = feeder.block;
					print(f"""
						"{id(feeder_block)}":"out_{register}":s ->
						"{id(block)}": "in_{register}":n [
							style = dashed
							constraint = false
							color = "{feeder_block.hue} 1 1"
						]
					""", file = stream);
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















