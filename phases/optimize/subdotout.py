
from debug import *;

from phases.self import phase;

def optimize_phase_subdotout(self, vrtovn, instruction, order_sensitive_instructions, expression_table):
	
	enter("optimize_phase_dotout()");
	
	stream = open(f"dot/{phase.frame_counter}-optimize.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black color=white fontcolor=white];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	""", file = stream);
	
	print(f"""
		label = "{str(instruction)}";
	""", file = stream);
	
	print("subgraph cluster_vr {", file = stream)
	
	print(f"""
		label = "";
	""", file = stream);
	
	for vr in vrtovn.keys():
		print(f"""
			"{vr}" [
				label="{vr}"
				{"style=bold" if vr == instruction.out else ""}
			];
		""", file = stream);
	
	print("}", file = stream)
	
	drawn = set();
	
	for vr, vn in vrtovn.items():
		if vn not in drawn:
			ex = expression_table.vntoex(vn);
			ex.dotout(stream, drawn = drawn, et = expression_table);
			drawn.add(vn);
		print(f"""
			"{vn}":s -> "{vr}":n [dir=back];
		""", file = stream);
	
	last = None;
	denominator = expression_table.valcounter;
	
	for inst in order_sensitive_instructions:
		for vn in inst.ins:
			if vn not in drawn:
				ex = expression_table.vntoex(vn);
				ex.dotout(stream, vn, drawn = drawn, et = expression_table);
				drawn.add(vn);
		
		label = inst.newdotout();
		
		if last:
			print(f"""
				"{last}":s -> "{label}":n [style=bold];
			""", file = stream);
		last = label;
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");














