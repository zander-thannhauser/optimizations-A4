
from debug import *;

from phases.self import phase;

def critical_phase_dotout(self, all_blocks, parameters, expression_table, **_):
	
	enter("critical_phase_dotout()");
	
	assert(not "TODO");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}")
	
	stream = open(f"dot/{phase.frame_counter}.txt", "w");
	
	assert(not "TODO");
	
#	print("""
#digraph mygraph {

#	node [shape=record];
#	
#	graph [bgcolor=black];
#	
#	edge [color=white]
#	
#	node [fontname="Courier New" fontcolor=white color=white];
#	
#	""", file = stream);
#	
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
#			assert(block.label);
#			head = block.label;
#			tail = block.label;
#		
#		headtails[id(block)] = (head, tail);
#	
#	for block in all_blocks:
#		head, tail = headtails[id(block)];
#		for s in block.successors:
#			print(f"""
#				"{tail}" -> "{headtails[id(s)][0]}" [color="white:black:white" style=bold];
#			""", file = stream);
#	
#	print("""
#}
#	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















