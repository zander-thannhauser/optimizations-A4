
from debug import *;

from phases.self import phase;

def in_out_phase_dotout(self, all_dots, all_blocks, **_):
	
	enter("in_out_phase_dotout()");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
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
		loc = " | ".join(block.loc);
		label = f"rpo = {block.rpo}";
		outs = " | ".join(block.outs);
		
		label = "{ { " + ins + "} | {" + loc + "} | " + label + " | { " + outs + " } }"
		
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















