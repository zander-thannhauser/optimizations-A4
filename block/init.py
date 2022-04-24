
def block_init(self, label, instructions, children_labels, jump = None):
	
	# used during reading assembly:
	self.label = label;
	self.instructions = instructions;
	self.jump = jump;
	self.children_labels = children_labels;
	self.order_sensitive_instructions = [];
	
	# after reading assembly:
	self.predecessors = [];
	self.successors = [];
	self.po  = 0;
	self.rpo = 0;
	self.hue = 0;
	
	# all phases:
	self.phase_counters = {
		"dead-code": 0,
	}
	
	# lost_parent phase:
	self.is_reachable = True;
	
	# in-out phase:
	self.ins = None; # set of registers
	self.outs = list(); # (register, instruction) tuples in *original* order
	
	# inheritance phase:
	self.given = None; # register -> set of sources
	
	# phi phase:
	self.incoming_phis = dict(); # register -> valnum
	self.outgoing_phis = dict(); # register -> set of phi valnums
	
	# optimize phase:
	self.vrtovn = None; # virtual register -> valnum
	self.avin = None;   # set of available valnums
	self.vnsrcs = None; # valnum -> set of (block, instruction-index) sources
	self.new_instructions = None;
	self.new_jump = None;
	
	# dominator phase:
	self.dominators = set();
	self.immediate_dominator = None;
	
	# post dominator phase:
	self.post_dominators = set();
	self.post_immediate_dominator = None;
	self.post_dominance_frontier = set();
	self.reverse_post_dominance_frontier = set();
	
	# critical phase:
	self.is_critical = False;
	




























