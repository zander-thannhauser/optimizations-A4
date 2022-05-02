
from debug import *;

from phases.self import phase;

def loop_depth_phase_dotout(self, all_blocks, expression_table, **_):
	
	enter("loop_depth.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-loop_depth.dot", "w");
	
	assert(not "TODO");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	max_depth = max(b.loop_depth for b in all_blocks if b.loop_depth is not None) + 1;
	
	for block in all_blocks:
		bid = id(block);
		
		if block.loop_depth is None:
			color = f"black"
		else:
			color = f"0 0 { block.loop_depth / max_depth }"
		
		print(f"""
			"{bid}" [
				label = "rpo = {block.rpo}"
				fillcolor = "{color}"
				color = white
				style = "filled{",bold" if block == self.block else ""}"
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























