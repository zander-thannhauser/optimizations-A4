
from debug import *;

def constant_dotout(self, stream, et, **_):
	hue = self.valnum / et.valcounter;
	print(f"""
		"{self.valnum}" [
			shape = circle
			label = "{self.value}"
			color = "{hue} 1 1"
		];
	""", file = stream);
