
from debug import *;

from phases.self import phase;

def available_phase_dotout(self, all_blocks, **_):
	
	enter("available_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-available.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	for block in all_blocks:
		bid = id(block);
		
		incoming = "|".join(str(a) for a in block.avout);
		local = "|".join(str(a) for a in block.avloc);
		killed = "|".join(str(a) for a in block.avkill);
		outgoing = "None" if block.avin is None else "|".join(str(a) for a in block.avin);
		
		label = "{{avout: | %s}|{avloc: | %s}|{avkill: | %s}|{avin: | %s}}" % \
			(incoming, local, killed, outgoing);
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{block.hue} 1 1"
				shape=record
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















