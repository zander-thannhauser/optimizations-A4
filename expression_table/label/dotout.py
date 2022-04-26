
from debug import *;

def label_dotout(self, stream, et, **_):
	hue = self.valnum / et.valcounter;
	print(f"""
		"{self.valnum}" [
			shape = square
			label = "{self.identifier}"
			color = "{hue} 1 1"
		];
	""", file = stream);
