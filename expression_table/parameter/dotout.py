
from debug import *;

def parameter_dotout(self, stream, et, **_):
	hue = self.valnum / et.valcounter;
	print(f"""
		"{self.valnum}" [
			shape = diamond
			label = "{self.register}"
			color = "{hue} 1 1"
		];
	""", file = stream);
