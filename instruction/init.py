
from instruction.self import instruction;

def instruction_init(self, op, ins, out = None, const = None, label = ""):
	self.op = op;
	self.ins = ins;
	self.out = out;
	self.const = const;
	self.label = label;
	self.id = instruction.counter;
	self.acting_i2i = False;
	self.is_critical = False;
	self.define_set = None;
	self.live_use_list = dict();
	instruction.counter += 1;


