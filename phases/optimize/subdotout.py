
from debug import *;

from phases.self import phase;

def optimize_phase_subdotout(self, vrtovn, avin, inst, new_instructions, expression_table):
	
	enter("optimize_phase_subdotout()");
	
	stream = open(f"dot/{phase.frame_counter}-optimize.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black color=white fontcolor=white];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	""", file = stream);
	
	print(f"""
		label = "{str(inst)}";
	""", file = stream);
	
	block = self.block;
	
	drawn = set();
	
	last = None;
	denominator = expression_table.valcounter;
	
	for inst in new_instructions:
		label = inst.newdotout(stream, block, constraint = True);
		
		if inst.out:
			drawn.add(inst.out);
		
		if last:
			print(f"""
				"{last}":s -> "{label}":n [style=bold];
			""", file = stream);
		last = label;
	
	for vn in vrtovn.values():
		if vn is not None and vn not in drawn:
			ex = expression_table.vntoex(vn);
			ex.dotout(stream, drawn = drawn, et = expression_table);
			drawn.add(vn);
	
	for inst in new_instructions:
		for vn in inst.ins:
			if vn not in drawn:
				ex = expression_table.vntoex(vn);
				ex.dotout(stream, drawn = drawn, et = expression_table);
				drawn.add(vn);
	
	for vr, vn in vrtovn.items():
		print(f"""
			"{vn}" -> "{vr}":n [dir=back];
		""", file = stream);
		print(f"""
			"{vr}" [
				label = "{vr}"
				shape = note
				{"style=filled fontcolor=black" if vr == inst.out else ""}
			];
		""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");














