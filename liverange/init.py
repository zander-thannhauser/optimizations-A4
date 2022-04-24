
from liverange.self import liverange;

def liverange_init(self, liveid):

	self.instance_id = liverange.instance_counter;
	self.liveid = liveid;
	
	self.definers = set(); # set of instructions
	self.users = set(); # set of instructions
	
	liverange.instance_counter += 1;
	

