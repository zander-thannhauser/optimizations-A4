
from debug import *;

from expression_table.constant.self   import constant;
from expression_table.expression.self import expression;
from expression_table.parameter.self  import parameter;
from expression_table.phi.self        import phi;
from expression_table.unknown.self    import unknown;

from phases.critical.self import critical_phase;

def critical_phase_process(self, **_):
	enter(f"critical_phase.process(instruction.id = {self.instruction.id})");
	
	todo = [];
	
	instruction = self.instruction;
	
	dprint(instruction);
	
	block = instruction.block;
	
	instruction.is_critical = True;
	
	if not block.is_critical:
		# push reverse_post_dominance_frontier's jumps:
		for split in block.reverse_post_dominance_frontier:
			assert(split.jump);
			if not split.jump.is_critical:
				todo.append(critical_phase(split.jump));
				split.jump.is_critical = True;
		block.is_critical = True;
	
	expression_table = block.expression_table;
	
	for valnum in instruction.ins:
		ex = expression_table.vntoex(valnum);
		match ex:
			case parameter():
				pass;
			
			case unknown():
				inst = ex.instruction;
				assert(inst);
				if not inst.is_critical:
					todo.append(critical_phase(inst));
					inst.is_critical = True;
			
			case phi() as p:
				if not p.is_critical:
					for feeder in p.feeders:
						if not feeder.is_critical:
							todo.append(critical_phase(feeder));
							feeder.is_critical = True;
					p.is_critical = True;
			
			case (constant() | expression()) as ex:
				inst = ex.instruction;
				assert(inst);
				if not inst.is_critical:
					todo.append(critical_phase(ex.instruction));
					inst.is_critical = True;
			
			case _:
				assert(not "TODO");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















