
from debug import *;

def phi_dotout(self, stream, et, **_):
	print(f"""
		"{self.valnum}" [
			shape = circle
			label = "ϕ"
			color = "{self.valnum / et.valcounter} 1 1"
		];
	""", file = stream);
