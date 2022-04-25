
from debug import *;

from phases.self import phase;

def allocate_register_phase_dotout(self, all_blocks, all_liveranges, num_registers, **_):
	
	enter("allocate_register.dotout()");
	
	dprint(f"phase.frame_counter = {phase.frame_counter}");
	
	stream = open(f"dot/{phase.frame_counter}-allocate_register.dot", "w");
	
	print("""
digraph mygraph {

	node [shape=box];
	
	graph [bgcolor=black];
	
	edge [color=white]
	
	node [fontname="Courier New" fontcolor=white color=white];
	
	""", file = stream);
	
	headtails = dict();
	allocation_headtails = dict();
	
	o, c = '{', '}';
	
	for block in all_blocks:
		
		head, tail = None, None;
		allocation_heads, allocation_tails = dict(), dict();
		
		for inst in block.newer_instructions + ([] if block.newer_jump is None else [block.newer_jump]):
			
			current = inst.newerdotout(stream);
			
			for n in range(num_registers):
				m = f"{id(inst)}_{n}";
				print(f"""
					"{m}" [
						label = ""
						shape = square
					];
					{o} rank = same; "{id(inst)}"; "{m}"; {c}
				""", file = stream);
				if n in allocation_tails:
					print(f"""
						"{allocation_tails[n]}" -> "{m}" [
							style = bold
						];
					""", file = stream);
				else:
					allocation_heads[n] = m;
				allocation_tails[n] = m;
			
			if tail:
				print(f"""
					"{tail}" -> "{current}" [
						style = bold
					];
				""", file = stream);
			else:
				head = current;
			
			tail = current;
		
		if not head:
			label = f"rpo = {block.rpo}";
			head = label;
			tail = label;
		
		headtails[id(block)] = (head, tail);
		allocation_headtails[id(block)] = (allocation_heads, allocation_tails);
	
	for block in all_blocks:
		head, tail = headtails[id(block)];
		
		for s in block.successors:
			print(f"""
				"{tail}" -> "{headtails[id(s)][0]}" [
					color = "white:black:white"
					style = bold
				];
			""", file = stream);
		
		allocation_heads, allocation_tails = allocation_headtails[id(block)];
		
		for s in block.successors:
			s_heads = allocation_headtails[id(s)][0];
			for n in range(num_registers):
				if n in allocation_tails and n in s_heads: print(f"""
					"{allocation_tails[n]}" -> "{s_heads[n]}" [
					];
				""", file = stream);
	
	for liverange in all_liveranges:
		if liverange.register is not None:
			liverange.newdotout(stream);
	
	print("""
}
	""", file = stream);
	
	stream.close();
	
	phase.frame_counter += 1;
	
	exit("return;");























