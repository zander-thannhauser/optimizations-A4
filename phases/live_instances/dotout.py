
from debug import *;

from phases.self import phase;

def live_instances_phase_dotout(self, all_blocks, all_liveranges, vnsets_to_liveid, **_):
	
	enter("live_instances.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-live_instances.dot", "w");
	
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
		liverange.dotout(stream, denominator);
	
	for liveid, liverange in self.block.liveout.items():
		print(f"""
			"{liveid}" [
				shape = note
				label = "%lr{liveid}"
			];
			"{id(liverange)}" -> "{liveid}" [
				dir = back
			];
		""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");























