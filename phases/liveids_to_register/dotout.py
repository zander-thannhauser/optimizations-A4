
from debug import *;

from phases.self import phase;

def liveids_to_register_phase_dotout(self, all_blocks, num_registers, **_):
	
	enter("liveids_to_register.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-liveids_to_register.dot", "w");
	
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
	
	headtails = dict();
	
	for block in all_blocks:
		
		head, tail = None, None;
		
		for inst in block.newer_instructions + ([] if block.newer_jump is None else [block.newer_jump]):
			
			current = inst.newestdotout(stream, num_registers);
			
			if tail:
				print(f"""
					"{tail}" -> "{current}" [
						style = bold
					];
				""", file = stream);
			else:
				head = current;
			
			tail = current;
		
		if not head:
			label = f"rpo = {block.rpo}";
			head = label;
			tail = label;
		
		headtails[id(block)] = (head, tail);
	
	for block in all_blocks:
		head, tail = headtails[id(block)];
		
		for s in block.successors:
			print(f"""
				"{tail}" -> "{headtails[id(s)][0]}" [
					color = "white:black:white"
					style = bold
				];
			""", file = stream);
		
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");























