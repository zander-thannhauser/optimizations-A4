
from debug import *;

from instruction.self import instruction;

from phases.rename_valnums_to_liveids.self import rename_valnums_to_liveids_phase;

def rename_valnums_to_liveids_phase_process(self, start, parameters, valnum_to_vnsets, vnsets_to_liveid, phase_counters, **_):
	enter(f"rename_valnums_to_liveids.process(self.block.rpo = {self.block.rpo})");
	
	block = self.block;
	
	todo = [];
	
	def get_id(valnum):
		vnset = tuple(sorted(valnum_to_vnsets[valnum]));
		if vnset in vnsets_to_liveid:
			return vnsets_to_liveid[vnset];
		else:
			next = vnsets_to_liveid["next"];
			vnsets_to_liveid[vnset] = next;
			vnsets_to_liveid["next"] = next + 1;
			return next;
	
	if block == start:
		for p in parameters:
			p.liveid = get_id(p.valnum);
	
	newer_instructions = [];
	
	last = None;
	for inst in block.new_instructions:
		new = instruction( \
			op = inst.op, \
			ins = [get_id(p) for p in inst.ins], \
			const = inst.const, \
			label = inst.label,
			out = (None if inst.out is None else get_id(inst.out)));
		
		new.block = block;
		
		if True \
			and last is not None \
			and last.op == "i2i" \
			and (last.op, last.ins, last.out) == (new.op, new.ins, new.out):
			# remove duplicate i2is:
			dprint(f"last = {last}")
			dprint(f"new = {new}")
		else:
			newer_instructions.append(new);
			last = new;
		
	
	block.newer_instructions = newer_instructions;
	
	if block.new_jump is not None:
		inst = block.new_jump;
		new = instruction( \
			op = inst.op, \
			ins = [get_id(p) for p in inst.ins], \
			label = inst.label);
		new.block = block;
		block.newer_jump = new;
	
	block.phase_counters["rename_valnums_to_liveids"] = phase_counters["rename_valnums_to_liveids"]
	
	for child in block.successors:
		if child.phase_counters["rename_valnums_to_liveids"] < phase_counters["rename_valnums_to_liveids"]:
			todo.append(rename_valnums_to_liveids_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;






















