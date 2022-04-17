
def block_init(self, label, original_instructions, children_labels, jump = None):
	
	# used during reading assembly:
	self.label = label;
	self.original_instructions = original_instructions;
	self.jump = jump;
	self.children_labels = children_labels;
	self.order_sensitive_instructions = [];
	
	# after reading assembly:
	self.predecessors = [];
	self.successors = [];
	self.po = 0;
	self.rpo = 0;
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
	self.given = dict(); # register -> set of sources
	
	# phi phase:
	self.incoming_phis = dict(); # register -> valnum
	self.outgoing_phis = dict(); # register -> set of phi valnums
	
	# optimize phase:
	self.vrtovn = None;
	
	# critical phase:
	self.is_critical = False;
	




























