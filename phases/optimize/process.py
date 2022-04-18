
from debug import *;

from phases.optimize.self import optimize_phase;
from phases.reset_dominators.self import reset_dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;

from expression_table.constant.self import constant;

from .instructions.add     import optimize_add;
from .instructions._and    import optimize_and;
from .instructions._assert import optimize_assert;
from .instructions.cbr     import optimize_cbr;
from .instructions.cbrne   import optimize_cbrne;
from .instructions.comp    import optimize_comp;
from .instructions.loadI   import optimize_loadI;
from .instructions.i2i     import optimize_i2i;
from .instructions.iwrite  import optimize_iwrite;
from .instructions.load    import optimize_load;
from .instructions.mod     import optimize_mod;
from .instructions.mult    import optimize_mult;
from .instructions._not    import optimize_not;
from .instructions._or     import optimize_or;
from .instructions.ret     import optimize_ret;
from .instructions.sub     import optimize_sub;
from .instructions.store   import optimize_store;
from .instructions.testeq  import optimize_testeq;
from .instructions.testge  import optimize_testge;
from .instructions.testgt  import optimize_testgt;
from .instructions.testle  import optimize_testle;
from .instructions.testlt  import optimize_testlt;

from instruction.self import instruction;

lookup = {
	"add":    optimize_add,
	"and":    optimize_and,
	"assert": optimize_assert,
	"cbr":    optimize_cbr,
	"cbrne":  optimize_cbrne,
	"comp":   optimize_comp,
	"i2i":    optimize_i2i,
	"iwrite": optimize_iwrite,
	"load":   optimize_load,
	"loadI":  optimize_loadI,
	"mod":    optimize_mod,
	"mult":   optimize_mult,
	"not":    optimize_not,
	"or":     optimize_or,
	"ret":    optimize_ret,
	"sub":    optimize_sub,
	"store":  optimize_store,
	"testeq": optimize_testeq,
	"testge": optimize_testge,
	"testgt": optimize_testgt,
	"testle": optimize_testle,
	"testlt": optimize_testlt,
};

def optimize_phase_process(self, start, expression_table, parameters, **_):
	enter(f"optimize_phase_process(block.po = {self.block.po})");
	
	todo = [];
	
	vrtovn = dict();
	
	block = self.block;
	
	if (block == start):
		for parameter in parameters:
			vrtovn[parameter.register] = parameter.valnum;
	else:
		for predecessor in block.predecessors:
			for register, valnum in predecessor.vrtovn.items():
				if register not in vrtovn:
					dprint(f"inherited {register} => {valnum} from {predecessor}");
					vrtovn[register] = valnum;
				else:
					assert(not "TODO");
		
		# introduce phi nodes entering this block into
		# the expression_table:
		for register, valnum in block.incoming_phis.items():
			vrtovn[register] = valnum;
		
		# process instructions, pushing order_sensitive:
		order_sensitive_instructions = [];
		
		for inst in block.instructions:
			dprint(inst);
			lookup[inst.op](
				vrtovn = vrtovn,
				ops = order_sensitive_instructions,
				expression_table = expression_table,
				ins = inst.ins,
				out = inst.out,
				const = inst.const,
				label = inst.label);
			self.subdotout(vrtovn, inst, order_sensitive_instructions, expression_table);
		
		# generate instructions for the expressions that
		# feed the i2is:
#		for register in block.outgoing_phis:
#			srcvn = expression_table.vrtovn(register);
#			srcex = expression_table.vntoex(subvalnum);
#			srcex.generate_instructions(subvalnum, expression_table, new_instructions);
#			assert(not "TODO");
		
		volatile = set();
		
		# generate the i2is, the order they were read in:
		for register in block.outs:
			if register in block.outgoing_phis:
				src_valnum = vrtovn[register];
				for dst_valnum in block.outgoing_phis[register]:
					dprint(f"register   = {register}")
					dprint(f"src_valnum = {src_valnum}")
					dprint(f"dst_valnum = {dst_valnum}")
					i2i = instruction("i2i", [src_valnum], dst_valnum);
					i2i.acting_i2i = True;
					dprint(i2i);
					phi = expression_table.vntoex(dst_valnum);
					phi.feeders.append(i2i);
					order_sensitive_instructions.append(i2i);
					volatile.add(dst_valnum);
		
		if block.jump is not None:
			before = block.jump
			
			jump = [];
			
			dprint(before);
			
			lookup[before.op](
				vrtovn = vrtovn,
				ops = order_sensitive_instructions,
				expression_table = expression_table,
				ins = inst.ins,
				out = inst.out,
				const = inst.const,
				label = inst.label,
				volatile = volatile);
			
			if len(jump):
#				after = order_sensitive_instructions[-1];
#				
#				dprint(f"before.op, after.op = {before.op, after.op}");
#				
#				match (before.op, after.op):
#					
#					case _ if before.op == after.op: pass;
#					
#					case ('cbr' | 'cbrne', 'cbr_GT' | 'cbr_GE'):
#						pass;
#					
#					case ('cbr', 'storeAI'):
#						block.jump = None;
#					
#					case _: assert(not "TODO");
				assert(not "TODO");
			else:
				block.jump = None;
			
			if block.jump is None:
				keep, lose = block.successors;
				lose.predecessors.remove(block);
				block.successors.remove(lose);
				# maybe it's unreachable now?
				todo.append(lost_parent_phase(lose));
				# for sure it's dominators have changed, reset and redo:
				todo.append(reset_dominators_phase(lose));
				# same with post-dominators:
				todo.append(reset_post_dominators_phase(block));
				# the things the parent needs to provide for it's children
				# might have changed:
				todo.append(in_out_phase(block));
				# the things the child can get from it's parent
				# might have changed:
				todo.append(inheritance_phase(lose));
				todo.append(phi_phase(lose));
				assert(not "TODO");
				
			assert(not "TODO");
		
		block.order_sensitive_instructions = order_sensitive_instructions;
	
	if block.vrtovn != vrtovn:
		for child in block.successors:
			todo.append(optimize_phase(child));
		block.vrtovn = vrtovn;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



































