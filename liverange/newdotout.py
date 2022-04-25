
import math;

def liverange_newdotout(self, stream):
	
	label = f"%lr{self.liveid}"
	
	color = f"{self.hue} 1 1";
	
	points = set.union(self.definers, self.users, self.interference_points);
	
	assert(self.register is not None);
	
	for p in points:
		print(f"""
			"{id(p)}_{self.register}" [
				label = "{label}"
				color = "{color}"
				style = filled
				fontcolor = black
			];
		""", file = stream);
	
	

