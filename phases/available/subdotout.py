
from debug import *;

from phases.self import phase;

def available_phase_subdotout(self, inst, avusers, avloc, avkill):
	
	stream = open(f"dot/{phase.frame_counter}-available.txt", "w");
	
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
	
	for usee, users in avusers.items():
		for user in users:
			print(f"""
				"{usee[1:]}" -> "{user[1:]}";
			""", file = stream);
	
	for dest in avloc:
		print(f"""
			"{dest[1:]}" [
				style = filled
				fillcolor = white
				fontcolor = black
			];
		""", file = stream);
	
	for dest in avkill:
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
	















