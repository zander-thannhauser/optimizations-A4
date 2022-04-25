
from liverange.self import liverange;

def liverange_init(self, liveid):

	self.instance_id = liverange.instance_counter;
	self.liveid = liveid;
	
	self.users = set(); # set of instructions
	self.definers = set(); # set of instructions
	self.interference_with = dict() # defintion instruction -> set of liveranges
	self.interference_points = set(); # set of instructions
	
	self.cost = None;
	self.register = None;
	self.hue = None;
	
	liverange.instance_counter += 1;
	

