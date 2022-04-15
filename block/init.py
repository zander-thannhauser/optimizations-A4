
def block_init(self, label, instructions, children_labels, jump = None):
	
	# used during reading assembly:
	self.label = label;
	self.instructions = instructions;
	self.jump = jump;
	self.children_labels = children_labels;
	
	# after reading assembly:
	self.predecessors = [];
	self.successors = [];
	self.po = 0;
	self.hue = 0;
	
	# all phases:
	self.phase_counters = {
		"reset-dominators": 0,
		"reset-post-dominators": 0,
		"in-out": 0,
		"inheritance": 0,
		"phi": 0,
		"optimize": 0,
		"dead-code": 0,
		"earliest": 0,
	}
	
	# lost_parent phase:
	self.is_reachable = True;
	
	# dominator phase:
	self.dominators = set();
	self.immediate_dominator = None;
	
	# post dominator phase:
	self.post_dominators = set();
	self.post_immediate_dominator = None;
	self.post_dominance_frontier = set();
	self.reverse_post_dominance_frontier = set();
	
	# in-out phase:
	self.ins = set(); # registers
	self.outs = list(); # (register, instruction) tuples in *original* order
	
	# inheritance phase:
	self.given = dict();
	
	# phi phase:
	self.incoming_phis = dict(); # register -> valnum
	self.outgoing_phis = dict();
	
	# optimize phase:
	pass
	
	# critical phase:
	self.is_critical = False;
	
	# available phase:
	self.avin = None;
	self.avusers = None;
	self.avloc = set();
	self.avout = set();
	self.avkill = set();
	
	# anticipation phase:
	self.antin = None;
	self.antout = set();
	self.antloc = set();
	self.antkill = set();
	
	# later phase:
	self.laterin = None;
	self.delete = set();






























