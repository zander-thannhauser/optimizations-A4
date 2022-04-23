
from debug import *;

from phases.self import phase;

from instruction.self import instruction;

def optimize_phase_dotout(self, all_blocks, expression_table, **_):
	
	enter("optimize_phase_dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-optimize.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	# optimize dotout():
	
	""", file = stream);
	
	headtails = dict();
	
	drawn = set();
	
	for block in all_blocks:
		
		for vn in block.incoming_phis.values():
			if vn not in drawn:
				phi = expression_table.vntoex(vn);
				phi.dotout(stream, done = drawn, et = expression_table);
				drawn.add(vn);
		
		head, tail = None, None;
		for inst in block.order_sensitive_instructions \
			+ ([] if block.new_jump is None else [block.new_jump]):
			
			for vn in inst.ins:
				if vn not in drawn:
					ex = expression_table.vntoex(vn);
					ex.dotout(stream, drawn = drawn, et = expression_table);
					drawn.add(vn);
			
			current = inst.newdotout(stream, constraint = True);
			
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
	
	# assert(not "CHECK");
	
	exit("return;");















