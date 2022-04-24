
from debug import *;

from phases.self import phase;

def build_interference_phase_dotout(self, all_blocks, all_liveranges, vnsets_to_liveid, interference, **_):
	
	enter("build_interference.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-build_interference.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	headtails = dict();
	
	denominator = vnsets_to_liveid["next"]
	
	for block in all_blocks:
		
		head, tail = None, None;
		
		for inst in block.newer_instructions + ([] if block.newer_jump is None else [block.newer_jump]):
			
			current = inst.newerdotout(stream, denominator);
			
			if tail:
				print(f"""
					"{tail}" -> "{current}" [style=bold];
				""", file = stream);
			else:
				head = current;
			
			tail = current;
		
		headtails[id(block)] = (head, tail);
	
	for block in all_blocks:
		head, tail = headtails[id(block)];
		
		for s in block.successors:
			print(f"""
				"{tail}" -> "{headtails[id(s)][0]}" [color="white:black:white" style=bold];
			""", file = stream);
	
	for liverange in all_liveranges:
		liverange.newdotout(stream, denominator);
	
	for a, b in interference:
		print(f"""
			"{id(a)}" -> "{id(b)}" [
				dir = none
			];
		""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");























