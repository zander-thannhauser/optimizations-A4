
from debug import *;

from phases.self import phase;

def valnum_singleton_sets_phase_dotout(self, valnum_to_vnsets, **_):
	
	enter("valnum_singleton_sets.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-valnum_singleton_sets.dot", "w");
	
	assert(not "TODO");
	
	filename = f"dot/{phase.frame_counter}-inout.dot";
	
	print(f"all_dots += {filename}", file = all_dots);
	
	stream = open(filename, "w");
	
	print("""
graph mygraph {

	node [shape=circle];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	layout = neato;
	
	""", file = stream);
	
	for vn, others in valnum_to_vnsets.items():
		
		print(f"""
			"{vn}" [
				
			];
		""", file = stream);
		
		for o in others:
			if o != vn: print(f"""
				"{vn}" -- "{o}" [
					
				];
			""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");























