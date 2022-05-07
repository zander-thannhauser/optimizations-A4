
from debug import *;

from phases.self import phase;

def dead_code_phase_dotout(self, all_blocks, parameters, expression_table, **_):
	
	enter("dead_code_phase_dotout()");
	
	assert(not "TODO");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	stream = open(f"dot/{phase.frame_counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	assert(not "TODO");
	
#	drawn_phis = set();
#	
#	for vn, param in enumerate(parameters):
#		param.dotout(stream, vn);
#	
#	headtails = dict();
#	
#	for block in all_blocks:
#		for valnum in block.incoming_phis.values():
#			if valnum not in drawn_phis:
#				phi = expression_table.vntoex(valnum);
#				phi.dotout(stream, valnum);
#				drawn_phis.add(valnum);
#		
#		head, tail = None, None;
#		for inst in block.instructions + ([block.jump] if block.jump else []):
#			current = inst.newdotout(stream);
#			if tail:
#				print(f"""
#					"{tail}" -> "{current}" [style=bold];
#				""", file = stream);
#			else:
#				head = current;
#			tail = current;
#		
#		if not head:
#			if block.label:
#				label = block.label;
#			else:
#				label = f"po = {block.po}";
#			head = label;
#			tail = label;
#		
#		headtails[id(block)] = (head, tail);
#	
#	for block in all_blocks:
#		dprint(f"block.po = {block.po}");
#		head, tail = headtails[id(block)];
#		for s in block.successors:
#			dprint(f"s.po = {s.po}")
#			print(f"""
#				"{tail}" -> "{headtails[id(s)][0]}" [color="white:black:white" style=bold];
#			""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















