
def phi_init(self, register, sources):
	self.register = register;
	self.sources = sources; # blocks[]
	self.feeders = dict(); # block -> instruction that feeds this phi node
	self.is_critical = False;

