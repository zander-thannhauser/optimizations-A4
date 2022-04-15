
import string

tokenchar1 = "._" "abcdefghijklmnopqrstuvwxyz" "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

tokenchar2 = tokenchar1 + "1234567890";

class tokenizer:
	def __init__(self, pathname):
		self.file = open(pathname, "r");
		self.c = self.file.read(1);
		self.token = None;
	
	def next(self):
		next(self);
	
	def __next__(self):
		self.token = "";
		
		def next():
			self.token = self.token + self.c;
			self.c = self.file.read(1);
			return self.c;
		
		while True:
			if self.c == "":
				token = None;
				break;
			elif self.c in [' ', '\t', '\n']:
				self.c = self.file.read(1);
			elif self.c == "#":
				while self.c and self.c != '\n':
					self.c = self.file.read(1);
			elif self.c == ',':
				next();
				break;
			elif self.c == ':':
				next();
				break;
			elif self.c == '=':
				assert(next() == '>');
				next();
				break;
			elif self.c == "\"":
				next();
				while self.c != "\"":
					if self.c != '\\':
						next();
					else:
						next();
						if '0' < self.c < '7':
							while '0' < self.c < '7':
								next();
						else:
							printf("self.c == '%c'\n", self.c);
							assert(not "TODO");
				next();
				break;
			elif self.c == "%":
				assert(next() == 'v');
				assert(next() == 'r');
				assert('0' <= next() <= '9');
				while '0' <= self.c <= '9':
					next();
				break;
			elif self.c == '-':
				if (next() == '>'):
					next();
				else:
					assert('0' <= self.c <= '9');
					while '0' <= self.c <= '9':
						next();
				break;
			elif '0' <= self.c <= '9':
				next();
				while self.c == '.' or '0' <= self.c <= '9':
					next();
				break;
			elif self.c in tokenchar1:
				token = "";
				while self.c in tokenchar2:
					next();
				break;
			else:
				printf("self.c == '%c'\n", self.c);
				assert(not "TODO");
		# printf("self.token == \"%s\"\n", self.token);
		return self.token;














