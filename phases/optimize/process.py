
from debug import *;

from phases.optimize.self import optimize_phase;
from phases.reset_dominators.self import reset_dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;

from expression_table.constant.self import constant;

from .instructions.add    import optimize_add;
from .instructions.cbr    import optimize_cbr;
from .instructions.cbrne  import optimize_cbrne;
from .instructions.comp   import optimize_comp;
from .instructions.loadI  import optimize_loadI;
from .instructions.i2i    import optimize_i2i;
from .instructions.iwrite import optimize_iwrite;
from .instructions.load   import optimize_load;
from .instructions.mult   import optimize_mult;
from .instructions.ret    import optimize_ret;
from .instructions.sub    import optimize_sub;
from .instructions.store  import optimize_store;
from .instructions.testge import optimize_testge;
from .instructions.testgt import optimize_testgt;
from .instructions.testle import optimize_testle;
from .instructions.testlt import optimize_testlt;

from instruction.self import instruction;

lookup = {
	"add":    optimize_add,
	"cbr":    optimize_cbr,
	"cbrne":  optimize_cbrne,
	"comp":   optimize_comp,
	"i2i":    optimize_i2i,
	"iwrite": optimize_iwrite,
	"load":   optimize_load,
	"loadI":  optimize_loadI,
	"mult":   optimize_mult,
	"ret":    optimize_ret,
	"sub":    optimize_sub,
	"store":  optimize_store,
	"testge": optimize_testge,
	"testgt": optimize_testgt,
	"testle": optimize_testle,
	"testlt": optimize_testlt,
};

def optimize_phase_process(self, expression_table, phase_counters, **_):
	enter(f"optimize_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	block = self.block;
	
	if block.label == ".frame":
		block.expression_table = expression_table.copy();
	else:
		block.expression_table = block.immediate_dominator.expression_table.copy();
		
		expression_table = block.expression_table;
		
		# introduce phi nodes entering this block into
		# the expression_table:
		for register, valnum in block.incoming_phis.items():
			expression_table.avrwvn(register, valnum);
		
		# process instructions, pushing order_sensitive:
		order_sensitive_instructions = [];
		for inst in block.instructions:
			dprint(inst);
			lookup[inst.op](
				ops = order_sensitive_instructions,
				ins = inst.ins,
				out = inst.out,
				const = inst.const,
				label = inst.label,
				expression_table = expression_table,
				todo = todo);
			self.subdotout(inst, order_sensitive_instructions, expression_table);
		
		# generate critical for the (possible) jump:
		if block.jump is not None:
			before = block.jump;
			volatile = set();
			
			for register, phi_valnums in block.outgoing_phis.items():
				for phi_valnum in phi_valnums:
					volatile.add(phi_valnum);
			
			dprint(before);
			
			lookup[before.op](
				ops = order_sensitive_instructions,
				ins = before.ins,
				out = before.out,
				const = before.const,
				label = before.label,
				expression_table = expression_table,
				volatile = volatile);
			
			if len(order_sensitive_instructions):
				after = order_sensitive_instructions[-1];
				
				dprint(f"before.op, after.op = {before.op, after.op}");
				
				match (before.op, after.op):
					
					case _ if before.op == after.op: pass;
					
					case ('cbr' | 'cbrne', 'cbr_GT' | 'cbr_GE'):
						pass;
					
					case ('cbr', 'storeAI'):
						block.jump = None;
					
					case _: assert(not "TODO");
			else:
				block.jump = None;
			
			if block.jump is None:
				keep, lose = block.successors;
				lose.predecessors.remove(block);
				block.successors.remove(lose);
				todo.append(reset_dominators_phase(lose));
				todo.append(reset_post_dominators_phase(block));
				phase_counters["reset-dominators"] += 1;
				phase_counters["reset-post-dominators"] += 1;
		
		# build new list of order_sensitive_instructions and instructions
		# that feed the order_sensitive_instructions:
		new_instructions = [];
		
		for osi in order_sensitive_instructions:
			# print(c);
			for vn in osi.ins:
				subex = expression_table.vntoex(vn);
				subex.generate_instructions(vn, expression_table, new_instructions);
			new_instructions.append(osi);
		
		# take jump instruction out of instruction list:
		if block.jump: block.jump = new_instructions.pop();
		
		# generate instructions for the expressions that
		# feed the i2is:
		for register in block.outgoing_phis:
			subvalnum = expression_table.vrtovn(register);
			subex = expression_table.vntoex(subvalnum);
			subex.generate_instructions(subvalnum, expression_table, new_instructions);
		
		# generate the i2is, the order they were read in:
		for register in block.outs:
			if register in block.outgoing_phis:
				src_valnum = expression_table.vrtovn(register);
				for dst_valnum in block.outgoing_phis[register]:
					dprint(f"register   = {register}")
					dprint(f"src_valnum = {src_valnum}")
					dprint(f"dst_valnum = {dst_valnum}")
					i2i = instruction("i2i", [src_valnum], dst_valnum);
					i2i.acting_i2i = True;
					dprint(i2i);
					phi = expression_table.vntoex(dst_valnum);
					phi.feeders.append(i2i);
					new_instructions.append(i2i);
		
		for i in new_instructions:
			i.block = block;
		
		if block.jump:
			block.jump.block = block;
		
		block.instructions = new_instructions;
	
	block.phase_counters["optimize"] = phase_counters["optimize"];
	
	for child in block.successors:
		if child.phase_counters["optimize"] < phase_counters["optimize"]:
			todo.append(optimize_phase(child));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















