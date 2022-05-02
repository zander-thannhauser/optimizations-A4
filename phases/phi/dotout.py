
from debug import *;

from expression_table.phi.self import phi;

from phases.self import phase;

def phi_phase_dotout(self, all_blocks, expression_table, all_dots, **_):
	
	enter("phi_phase_dotout()");
	
	filename = f"dot/{phase.frame_counter}-phi.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	def draw_phi(valnum, reg):
		hue = valnum / expression_table.valcounter;
		exp = expression_table.vntoex(valnum);
		
		assert(type(exp) is phi);
		
		print(f"""
			"{valnum}" [
				label="𝜙"
				shape=doublecircle
				color="{hue} 1 1"
			];
		""", file = stream);
		
		for srcblock in exp.sources:
			print(f"""
				"{id(srcblock)}":"out_{reg[1:]}":s -> "{valnum}"
				 [style=dashed color="{srcblock.hue} 1 1"];
			""", file = stream);
	
	drawn_phis = set();
	
	print("""
digraph mygraph {

	node [shape=record];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	
	for block in all_blocks:
		bid = id(block);
		
		ins = " | ".join(f"<in_{r[1:]}> {r}" for r in block.ins);
		
		label = f"rpo = {block.rpo}";
		
		outs = " | ".join(f"<out_{r[1:]}> {r}" for r in block.outs);
		
		label = "{ { " + ins + "} | " + label + " | { " + outs + " } }"
		
		
		print(f"""
			"{bid}" [
				label="{label}"
				color="{block.hue} 1 1"
				{"style=bold" if block == self.block else ""}
			];
		""", file = stream);
		
		for c in block.successors:
			print(f"\"{bid}\":s -> \"{id(c)}\":n [style=bold]", file = stream);
		
		for reg in block.given:
			if reg in block.incoming_phis:
				
				valnum = block.incoming_phis[reg];
				if valnum not in drawn_phis:
					draw_phi(valnum, reg);
					drawn_phis.add(valnum);
				
				hue = valnum / expression_table.valcounter;
				print(f"""
					"{valnum}" -> "{id(block)}":"in_{reg[1:]}":n
					 [style=dashed color="{hue} 1 1"];
				""", file = stream);
			else:
				feeders = block.given[reg];
				for feeder in feeders:
					predecessor = feeder;
					print(f"""
						"{id(predecessor)}":"out_{reg[1:]}":s ->
						"{id(block)}":      "in_{reg[1:]}" :n
						 [style=dashed color="{predecessor.hue} 1 1"]
					""", file = stream);
		
		
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");















