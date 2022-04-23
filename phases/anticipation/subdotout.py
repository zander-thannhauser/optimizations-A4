
from debug import *;

from phases.self import phase;

def anticipation_phase_subdotout(self, inst, antusers, antloc, antkill):
	
	stream = open(f"dot/{phase.frame_counter}-anticipation.txt", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [fontcolor=white bgcolor=black];
	
	edge [color=white]
	
	node [fontcolor=white color=white];
	
	""", file = stream);
	
	print(f"""
		label = "{str(inst)}"
	""", file = stream);
	
	block = self.block;
	
	for usee, users in antusers.items():
		for user in users:
			print(f"""
				"{usee[1:]}" -> "{user[1:]}";
			""", file = stream);
	
	for dest in antloc:
		print(f"""
			"{dest[1:]}" [
				style = filled
				fillcolor = white
				fontcolor = black
			];
		""", file = stream);
	
	for dest in antkill:
		print(f"""
			"{dest[1:]}" [
				color = red
				penwidth = 3
			];
		""", file = stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	















