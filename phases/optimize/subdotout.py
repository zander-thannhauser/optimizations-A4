
from debug import *;

from phases.self import phase;

def optimize_phase_subdotout(self, instruction, order_sensitive_instructions, expression_table):
	
	enter("optimize_phase_dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	dprint(f"self.frame_counter  = {self.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-{self.frame_counter}.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black color=white fontcolor=white];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	# optimize subdotout():
	
	""", file = stream);
	
	print("subgraph cluster_vr {", file = stream)
	
	print(f"""
		label = "{str(instruction)}";
	""", file = stream);
	
	for vr in expression_table._vrtovn.keys():
		print(f"""
			{vr[1:]} [
				label="{vr}"
				{"style=bold" if vr in instruction.ins else ""}
				{"style=bold" if vr == instruction.out else ""}
			];
		""", file = stream);
	
	print("}", file = stream)
	
	drawn = set();
	
	for vr, vn in expression_table._vrtovn.items():
		if vn not in drawn:
			ex = expression_table.vntoex(vn);
			ex.dotout(stream, vn, done = drawn, expression_table = expression_table);
			drawn.add(vn);
		print(f"""
			{vr[1:]}:s -> "{vn}":n;
		""", file = stream);
	
	last = None;
	
	denominator = expression_table.valcounter;
	
	for inst in order_sensitive_instructions:
		label = id(inst);
		
		for vn in inst.ins:
			if vn not in drawn:
				ex = expression_table.vntoex(vn);
				ex.dotout(stream, vn, done = drawn, expression_table = expression_table);
				drawn.add(vn);
			
		match inst.op:
			case "storeAI":
				val, adr = inst.ins;
				off = inst.const;
				print(f"""
					"{label}" [
						shape = record
						color = white
						label = "storeAI | <val> %vr{val} | ⟶ | <adr> %vr{adr} | <off> {off}"
					];
					
					"{val}":s -> "{label}":val:n [color="{val / denominator} 1 1"];
					"{adr}":s -> "{label}":adr:n [color="{adr / denominator} 1 1"];
					
				""", file = stream);
			
			case "storeAO":
				val, adr, off = inst.ins;
				print(f"""
					"{label}" [
						shape = record
						color = white
						label = "storeAI | <val> %vr{val} | ⟶ | <adr> %vr{adr} | <off> %vr{off}"
					];
					
					"{val}":s -> "{label}":val:n [color="{val / denominator} 1 1"];
					"{adr}":s -> "{label}":adr:n [color="{adr / denominator} 1 1"];
					"{off}":s -> "{label}":off:n [color="{off / denominator} 1 1"];
					
				""", file = stream);
			
			case "loadAO":
				ptr, index = inst.ins;
				dest = inst.out;
				print(f"""
					"{label}" [
						shape = record
						color = "{dest / denominator} 1 1"
						label = "loadAO | <ptr> %vr{ptr} | <index> %vr{index}"
					];
					
					"{ptr}":s   -> "{label}":ptr:n [color="{ptr / denominator} 1 1"];
					"{index}":s -> "{label}":index:n [color="{index / denominator} 1 1"];
					
				""", file = stream);
			
			case "iwrite":
				ptr, = inst.ins;
				print(f"""
					"{label}" [
						shape = record
						color = "white"
						label = "iwrite | <ptr> %vr{ptr}"
					];
					
					"{ptr}":s -> "{label}":ptr:n [color="{ptr / denominator} 1 1"];
					
				""", file = stream);
			
			case _:
				dprint(f"inst.op = {inst.op}")
				assert(not "TODO");
		
		if last:
			print(f"""
				"{last}":s -> "{label}":n [style=bold];
			""", file = stream);
		last = label;
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	self.frame_counter += 1;
	
	dprint(f"self.frame_counter = {self.frame_counter}")
	
	exit("return;");














