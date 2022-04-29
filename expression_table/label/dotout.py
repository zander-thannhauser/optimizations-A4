
from debug import *;

def label_dotout(self, stream, et, **_):
	hue = self.valnum / et.valcounter;
	print(f"""
		"{self.valnum}" [
			shape = box
			label = "{self.identifier}"
			color = "{hue} 1 1:white:{hue} 1 1"
		];
	""", file = stream);
