
from debug import *;

from phases.lost_parent.self import lost_parent_phase;
from phases.reset_dominators.self import reset_dominators_phase;
from phases.reset_post_dominators.self import reset_post_dominators_phase;
from phases.reset_in_out.self import reset_in_out_phase;
from phases.inheritance.self import inheritance_phase;
from phases.phi.self import phi_phase;
from phases.optimize.self import optimize_phase;

from expression_table.constant.self import constant;

from .instructions.add     import optimize_add;
from .instructions._and    import optimize_and;
from .instructions._assert import optimize_assert;
from .instructions.call    import optimize_call;
from .instructions.cbr     import optimize_cbr;
from .instructions.cbrne   import optimize_cbrne;
from .instructions.comp    import optimize_comp;
from .instructions.f2i     import optimize_f2i;
from .instructions.fadd    import optimize_fadd;
from .instructions.fload   import optimize_fload;
from .instructions.fmult   import optimize_fmult;
from .instructions.loadI   import optimize_loadI;
from .instructions.i2i     import optimize_i2i;
from .instructions.i2f     import optimize_i2f;
from .instructions.icall   import optimize_icall;
from .instructions.iret    import optimize_iret;
from .instructions.iread   import optimize_iread;
from .instructions.iwrite  import optimize_iwrite;
from .instructions.load    import optimize_load;
from .instructions.mod     import optimize_mod;
from .instructions.mult    import optimize_mult;
from .instructions._not    import optimize_not;
from .instructions._or     import optimize_or;
from .instructions.putchar import optimize_putchar;
from .instructions.ret     import optimize_ret;
from .instructions.rshift  import optimize_rshift;
from .instructions.sub     import optimize_sub;
from .instructions.store   import optimize_store;
from .instructions.swrite  import optimize_swrite;
from .instructions.testeq  import optimize_testeq;
from .instructions.testge  import optimize_testge;
from .instructions.testgt  import optimize_testgt;
from .instructions.testle  import optimize_testle;
from .instructions.testlt  import optimize_testlt;
from .instructions.testne  import optimize_testne;

from instruction.self import instruction;

lookup = {
	"add":     optimize_add,
	"and":     optimize_and,
	"assert":  optimize_assert,
	"call":    optimize_call,
	"cbr":     optimize_cbr,
	"cbrne":   optimize_cbrne,
	"comp":    optimize_comp,
	"f2i":     optimize_f2i,
	"fadd":    optimize_fadd,
	"fload":   optimize_fload,
	"fmult":   optimize_fmult,
	"i2i":     optimize_i2i,
	"i2f":     optimize_i2f,
	"icall":   optimize_icall,
	"iret":    optimize_iret,
	"iread":   optimize_iread,
	"iwrite":  optimize_iwrite,
	"load":    optimize_load,
	"loadI":   optimize_loadI,
	"mod":     optimize_mod,
	"mult":    optimize_mult,
	"not":     optimize_not,
	"or":      optimize_or,
	"putchar": optimize_putchar,
	"ret":     optimize_ret,
	"rshift":  optimize_rshift,
	"sub":     optimize_sub,
	"store":   optimize_store,
	"swrite":  optimize_swrite,
	"testeq":  optimize_testeq,
	"testge":  optimize_testge,
	"testgt":  optimize_testgt,
	"testle":  optimize_testle,
	"testlt":  optimize_testlt,
	"testne":  optimize_testne,
};

def optimize_phase_process(self, start, expression_table, parameters, **_):
	enter(f"optimize_phase_process(block.rpo = {self.block.rpo})");
	
	todo = [];
	
	vrtovn = dict();
	
	block = self.block;
	
	if not block.is_reachable:
		exit();
		return [];
	
	avin = set();
	
	if (block == start):
		for parameter in parameters:
			vrtovn[parameter.register] = parameter.valnum;
			avin.add(parameter.valnum);
		block.new_instructions = [];
	else:
		for predecessor in block.predecessors:
			if predecessor.vrtovn is not None:
				for register, valnum in predecessor.vrtovn.items():
					if register not in vrtovn:
						dprint(f"inherited {register} => {valnum} from {predecessor}");
						vrtovn[register] = valnum;
					elif vrtovn[register] is not None and vrtovn[register] != valnum:
						dprint(f"conflicting valnum for {register} from {predecessor}");
						vrtovn[register] = None;
			else:
				dprint(f"inherited nothing from {predecessor}");
		
		avin = block.immediate_dominator.avin.copy();
		
		# introduce phi nodes entering this block into
		# the expression_table:
		for register, valnum in block.incoming_phis.items():
			dprint(f"inherited {register} => {valnum} from phi nodes");
			vrtovn[register] = valnum;
			avin.add(valnum);
		
	dprint(f"avin = {avin}");
	
	# process instructions, pushing order_sensitive:
	new_instructions = [];
	
	for inst in block.instructions:
		dprint(inst);
		lookup[inst.op](
			avin = avin,
			id = inst.id,
			ins = inst.ins,
			out = inst.out,
			vrtovn = vrtovn,
			const = inst.const,
			label = inst.label,
			ops = new_instructions,
			expression_table = expression_table);
		self.subdotout(vrtovn, avin, inst, new_instructions, expression_table);
	
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
				phi.feeders[block] = i2i;
				new_instructions.append(i2i);
				volatile.add(dst_valnum);
				self.subdotout(vrtovn, avin, i2i, new_instructions, expression_table);
	
	if block.jump is not None:
		before = block.jump
		
		jump = [];
		
		dprint(before);
		
		lookup[before.op](
			ops = jump,
			vrtovn = vrtovn,
			avin = avin,
			id = before.id,
			ins = before.ins,
			out = before.out,
			const = before.const,
			label = before.label,
			expression_table = expression_table,
			volatile = volatile);
		
		self.subdotout(vrtovn, avin, before, new_instructions + jump, expression_table);
		
		if len(jump):
			after, = jump
			
			dprint(f"before.op, after.op = {before.op, after.op}");
			
			match (before.op, after.op):
				
				case _ if before.op == after.op: pass;
				
				case ('cbr' | 'cbrne',
				      'cbr' | 'cbrne' | 'cbr_LT' | 'cbr_GT' | 'cbr_GE' | 'cbr_EQ' | 'cbr_LE' | 'cbr_NE' | 'cbr_EQ'):
					pass;
				
				# always jump:
				case ('cbr', 'jumpI'):
					lose, keep = block.successors;
					block.jump = None;
				
				case _: assert(not "TODO");
			
			after.block = block;
			block.new_jump = after;
		else:
			# always fallthrough:
			keep, lose = block.successors;
			block.jump = None;
		
		if block.jump is None:
			dprint(f"keep, lose = {str(keep), str(lose)}")
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
			todo.append(reset_in_out_phase(block));
			# the things the child can get from it's parent
			# might have changed:
			todo.append(inheritance_phase(lose));
			todo.append(phi_phase(lose));
			block.new_jump = None;
	
	for n in new_instructions:
		n.block = block;
	
	block.new_instructions = new_instructions;
	
	dprint(f"block.vrtovn = {block.vrtovn}")
	dprint(f"vrtovn       = {vrtovn}")
	
	dprint(f"block.avin = {block.avin}")
	dprint(f"avin       = {avin}")
	
	if False \
		or block.vrtovn != vrtovn \
		or block.avin != avin:
		
		for child in block.successors:
			todo.append(optimize_phase(child));
		
		block.vrtovn = vrtovn;
		block.avin = avin;
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;



































