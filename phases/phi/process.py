
from debug import *;

from expression_table.phi.self import phi;

from phases.optimize.self import optimize_phase;

def phi_phase_process(self, expression_table, **_):
	enter(f"phi_phase.process(block.po = {self.block.po})");
	
	block = self.block;
	
	todo = [];
	
	changed = False;
	
	for register, newsrcs in block.given.items():
		dprint(f"register = {register}, newsrcs = {[str(s) for s in newsrcs]}");
		
		if not len(newsrcs):
			fprintf(stderr, "use of undefined register!");
			sys.exit(1);
		
		# what's old?
		if (old := block.incoming_phis.get(register)) is None:
			oldsrcs = set();
		else:
			# whatever comes from the phi node
			oldphi = expression_table.vntoex(old);
			oldsrcs = oldphi.sources;
			dprint(f"oldsrcs = {[str(o) for o in oldsrcs]}");
		
		# what's new?
		if len(newsrcs) > 1:
			exp = phi(register, newsrcs);
			result = expression_table.extovn(exp);
			new = result.valnum;
			dprint(f"newsrcs = {[str(n) for n in newsrcs]}");
		else:
			new = None;
			newsrcs = set();
		
		dprint(f"old = {old}");
		dprint(f"new = {new}");
		
		if new != old:
			# remove old:
			for oldsrc in oldsrcs:
				writetos = oldsrc.outgoing_phis[register];
				writetos.discard(old);
				todo.append(optimize_phase(oldsrc));
			
			# add new:
			for newsrc in newsrcs:
				writetos = newsrc.outgoing_phis.setdefault(register, set());
				writetos.add(new);
				todo.append(optimize_phase(newsrc));
			
			if new is None:
				del block.incoming_phis[register];
			else:
				block.incoming_phis[register] = new;
			
			changed = True;
	
	if changed:
		todo.append(optimize_phase(block));
	
	exit(f"return {[str(t) for t in todo]}");
	return todo;















