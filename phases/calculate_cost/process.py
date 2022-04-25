
from debug import *;

from phases.calculate_cost.self import calculate_cost_phase;
from phases.allocate_register.self import allocate_register_phase;

def calculate_cost_phase_process(self, interference, **_):
	enter(f"calculate_cost.process(self.liverange = {self.liverange})");
	
	lr = self.liverange;
	
	cost = 0;
	
	if lr.liveid == 0:
		cost = float('inf');
	
	if (len(lr.definers), len(lr.users)) == (1, 1):
		definer, = lr.definers;
		user, = lr.users;
		if definer.block == user.block:
			block = definer.block;
			definer_index = block.newer_instructions.index(definer);
			if user in block.newer_instructions:
				user_index = block.newer_instructions.index(user);
			else:
				assert(user == block.newer_jump);
				user_index = len(block.newer_instructions);
			dprint(f"definer_index, user_index = {definer_index, user_index}")
			if definer_index + 1 == user_index:
				cost = 1000000000;
	
	if len(lr.definers) == 1 and list(lr.definers)[0].op == "loadI":
		for inst in lr.users:
			block = inst.block;
			cost += 10 ** block.loop_depth;
	else:
		for inst in set.union(lr.definers, lr.users):
			block = inst.block;
			cost += 10 ** block.loop_depth;
	
	dprint(f"cost = {cost}")
	
	benefit = sum(lr in t for t in interference);
	
	dprint(f"benefit = {benefit}");
	
	lr.cost = cost / benefit if benefit else cost;
	
	dprint(f"lr.cost = {lr.cost}");
	
	todo = [];
	
	todo.append(allocate_register_phase(lr));
	
	exit();
	return todo;






















