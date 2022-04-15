
from debug import *;

from phases.self import phase;

from instruction.self import instruction;

def optimize_phase_dotout(self, all_blocks, expression_table, parameters, phase_counters, **_):
	
	enter("optimize_phase_dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	dprint(f"self.frame_counter  = {self.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-optimize.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	# optimize dotout():
	
	""", file = stream);
	
	drawn_phis = set();
	
	for vn, param in enumerate(parameters):
		param.dotout(stream, vn);
	
	headtails = dict();
	
	for block in all_blocks:
		for valnum in block.incoming_phis.values():
			if valnum not in drawn_phis:
				phi = expression_table.vntoex(valnum);
				phi.dotout(stream, valnum, done = drawn_phis, expression_table = expression_table);
				drawn_phis.add(valnum);
		
		if block.phase_counters["optimize"] == phase_counters["optimize"]:
			callme = instruction.newdotout;
		else:
			callme = instruction.dotout;
		
		head, tail = None, None;
		for inst in block.instructions + ([block.jump] if block.jump else []):
			current = callme(inst, stream);
			if tail:
				print(f"""
					"{tail}" -> "{current}" [style=bold];
				""", file = stream);
			else:
				head = current;
			tail = current;
		
		if not head:
			assert(block.label);
			head = block.label;
			tail = block.label;
		
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















