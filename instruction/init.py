
from instruction.self import instruction;

def instruction_init(self, op, vr_ins, vr_out = None, const = None, label = ""):
	
	self.id = instruction.counter;
	
	self.op = op;
	self.vr_ins = vr_ins;
	self.vr_out = vr_out;
	self.const = const;
	self.label = label;
	
	self.is_critical = False;
	
	self.define_set = None;
	self.live_use_list = dict();
	
	instruction.counter += 1;


