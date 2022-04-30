
from debug import *;

from phases.self import phase;

def insert_delete_phase_dotout(self, all_blocks, **_):
	
	enter("insert_delete_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-insert_delete.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	headtails = dict();
	
	for block in all_blocks:
		bid = id(block);
		
		head, tail = None, None;
		
		for inst in block.original_instructions + ([] if block.jump is None else [block.jump]):
			
			current = inst.dotout(stream, block);
			
			if tail:
				print(f"""
					"{tail}" -> "{current}" [style=bold];
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
		match len(block.successors):
			case 0:
				pass
			case 1:
				s, = block.successors;
				print(f"""
					"{tail}" -> "{headtails[id(s)][0]}" [color="white:black:white" style=bold];
				""", file = stream);
			case 2:
				l, r = block.successors;
				print(f"""
					"{tail}":w -> "{headtails[id(l)][0]}" [color="white:black:white" style=bold];
					"{tail}":e -> "{headtails[id(r)][0]}" [color="white:black:white" style=bold];
				""", file = stream);
			case _:
				assert(not "TODO");
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















