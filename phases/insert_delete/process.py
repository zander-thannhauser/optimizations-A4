
from debug import *;

from block.self import block;

from phases.insert_delete.self import insert_delete_phase;

counter = 0;

def insert_delete_phase_process(self, insert, syntax_lookup, phase_counters, all_blocks, **_):
	enter(f"insert_delete_phase_process(block.rpo = {self.block.rpo})");
	
	global counter;
	
	b = self.block;
	
	for p in b.predecessors:
		if raw_outs := insert[(p, b)]:
			
			raw_instructions = [syntax_lookup[out] for out in raw_outs];
			
			for i, e in enumerate(raw_instructions):
				dprint(f"raw_instructions[{i}] = {raw_instructions[i]}");
			
			instructions = [];
			
			outs = {inst.out: inst for inst in raw_instructions};
			
			def helper(inst):
				for i in inst.ins:
					if i in outs:
						helper(outs[i]);
				instructions.append(inst);
			
			for inst in raw_instructions:
				if inst not in instructions:
					helper(inst);
			
			for i, e in enumerate(instructions):
				dprint(f"instructions[{i}] = {instructions[i]}");
			
			edge_block = block( \
				label = "", \
				instructions = instructions, \
				children_labels = [b.label],\
				jump = None)
			
			edge_block.po  = (b. po[0], b.subparent_po)
			edge_block.rpo = (p.rpo[0], p.subchild_rpo)
			
			edge_block.predecessors = [p];
			edge_block.successors = [b];
			
			p.subparent_po += 1;
			b.subchild_rpo += 1;
			
			p.successors[(pb_index := p.successors.index(b))] = edge_block;
			b.predecessors[b.predecessors.index(p)] = edge_block;
			
			if p.jump is not None and pb_index > 0:
				edge_block.label = f".subblock_{counter}";
				assert(b.label and p.jump.label == b.label);
				p.jump.label = edge_block.label;
				counter += 1;
			
			all_blocks.append(edge_block);
	
	for d in b.delete:
		b.original_instructions = [i for i in b.original_instructions if i.out != d];
	
	b.phase_counters["insert-delete"] = phase_counters["insert-delete"];
	
	todo = [];
	
	for child in b.successors:
		if child.phase_counters["insert-delete"] < phase_counters["insert-delete"]:
			todo.append(insert_delete_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















