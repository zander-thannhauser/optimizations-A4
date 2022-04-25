
#def liverange_newdotout(self, stream, denominator):
#	
#	label = f"%lr{self.liveid}"
#	
#	o, c = '{', '}';
#	
#	hue = self.liveid / denominator;
#	
#	last = None;
#	
#	for i, inst in enumerate(sorted(set.union(self.definers, self.users))):
#		name = f"{id(self)}_{i}";
#		
#		print(f"""
#			"{name}" [
#				shape = {"doublecircle" if inst in self.definers else "circle"}
#				label = "{label}"
#				color = "{hue} 1 1"
#			];
#			
#			{o}
#				rank = same;
#				"{id(inst)}"; "{name}";
#			{c}
#		""", file = stream);
#		
#		if last is not None:
#			print(f"""
#				"{last}" -> "{name}" [
#					dir = none
#				];
#			""", file = stream);
#			
#		last = name;
#	
#	
