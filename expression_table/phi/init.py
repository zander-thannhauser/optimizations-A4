
def phi_init(self, register, sources):
	self.register = register;
	self.sources = sources; # blocks[]
	self.feeders = list(); # instructions that feed this phi node
	self.is_critical = False;

