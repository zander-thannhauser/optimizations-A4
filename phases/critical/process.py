
from debug import *;

from expression_table.phi.self        import phi;
from expression_table.label.self      import label;
from expression_table.unknown.self    import unknown;
from expression_table.constant.self   import constant;
from expression_table.expression.self import expression;
from expression_table.parameter.self  import parameter;

from phases.critical.self import critical_phase;

def critical_phase_process(self, expression_table, **_):
	enter(f"critical_phase.process(instruction.id = {self.instruction.id})");
	
	todo = [];
	
	instruction = self.instruction;
	
	dprint(f"instruction: {instruction}");
	
	block = instruction.block;
	
	dprint(f"block = {block}")
	assert(block is not None);
	
	instruction.is_critical = True;
	
	if not block.is_critical:
		# push reverse_post_dominance_frontier's jumps:
		for split in block.reverse_post_dominance_frontier:
			assert(split.new_jump);
			if not split.new_jump.is_critical:
				todo.append(critical_phase(split.new_jump));
				split.new_jump.is_critical = True;
		block.is_critical = True;
	
	for valnum in instruction.ins:
		ex = expression_table.vntoex(valnum);
		
		match ex:
			case parameter():
				pass;
			
			case phi() as p:
				if not p.is_critical:
					for feeder in p.feeders.values():
						if not feeder.is_critical:
							todo.append(critical_phase(feeder));
							feeder.is_critical = True;
					p.is_critical = True;
			
			case (label() | unknown() | constant() | expression()) as ex:
				finger = block;
				found = None;
				
				while found is None and finger != finger.immediate_dominator:
					dprint(f"finger = {finger}")
					for inst in finger.new_instructions[::-1]:
						if inst.out == valnum:
							found = inst;
					dprint(f"finger.immediate_dominator = {finger.immediate_dominator}")
					finger = finger.immediate_dominator;
				
				assert(found);
				
				if not found.is_critical:
					todo.append(critical_phase(found));
					found.is_critical = True;
				
			case _:
				assert(not "TODO");
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















