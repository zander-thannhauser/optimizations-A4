
def block_init(self, label, instructions, children_labels, jump = None):
	
	# used during reading assembly:
	self.label = label;
	self.original_instructions = instructions;
	self.jump = jump;
	self.children_labels = children_labels;
	self.order_sensitive_instructions = [];
	
	# after reading assembly:
	self.predecessors = [];
	self.successors = [];
	self.edges_from_start = 1000;
	self.edges_from_end = 1000;
	self.po  = 0;
	self.rpo = 0;
	self.hue = 0;
	
	# all phases:
	self.phase_counters = {
		"syntax-lookup": 0,
		"earliest": 0,
		"insert-delete": 0,
		"superfical-critical": 0,
		"dead-code": 0,
		"valnum_singleton_sets": 0,
		"union_valnum_sets": 0,
		"rename_valnums_to_liveids": 0,
		"build_interference": 0,
		"remove_i2is": 0,
	}
	
	# lost_parent phase:
	self.is_reachable = True;
	
	# available phase:
	self.avin = None;
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
	
	# insert & delete:
	self.subparent_po = 1;
	self.subchild_rpo = 1;
	
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
	
	# loop-depth phase:
	self.loop_depth = None;
	self.public_loop_depth = None;
	
	# rename_valnums_to_liveids:
	self.newer_instructions = [];
	self.newer_jump = None;
	
	# live_in_out:
	self.live_ins = None;
	self.live_outs = dict();
	
	# live_inheritance:
	self.live_given = None;
	
	# live_instances:
	self.liveout = None;
	
	# build_interference:
	
	# remove i2is:
	self.newest_instructions = [];
	self.newest_jump = None;



























