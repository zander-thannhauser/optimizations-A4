
from debug import *;

from phases.self import phase;

def dead_code_phase_dotout(self, all_blocks, parameters, expression_table, **_):
	
	enter("dead_code_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-deadcode.dot", "w");
	
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
		
		for inst in block.new_instructions + ([] if block.new_jump is None else [block.new_jump]):
			
			current = inst.newdotout(stream, valnum_names = False, draw_lines = False);
			
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
		
		for s in block.successors:
			print(f"""
				"{tail}" -> "{headtails[id(s)][0]}" [color="white:black:white" style=bold];
			""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















