
from debug import *;

from expression_table.phi.self import phi;

from phases.phi.self import phi_phase;

def phi_phase_process(self, expression_table, phase_counters, **_):
	enter(f"phi_phase.process(block.po = {self.block.po})");
	
	block = self.block;
	
	for register, srcblocks in block.given.items():
		dprint(f"register = {register}, srcblocks = {[str(s) for s in srcblocks]}");
		if not len(srcblocks):
			fprintf(stderr, "use of undefined register!");
			sys.exit(1);
		elif len(srcblocks) > 1:
			exp = phi(register, srcblocks);
			result = expression_table.extovn(exp);
			block.incoming_phis[register] = result.valnum;
			if result.is_new:
				for srcblock in srcblocks:
					srcblock.outgoing_phis.setdefault(register, []).append(result.valnum);
	
	# needs to invoke optimize on the affected blocks
	
	todo = [];
	
	block.phase_counters["phi"] = phase_counters["phi"];
	
	for successor in block.successors:
		if successor.phase_counters["phi"] < phase_counters["phi"]:
			todo.append(phi_phase(successor));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















