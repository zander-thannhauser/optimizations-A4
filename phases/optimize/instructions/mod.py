
# match (rexp, lexp):
	
	# (constant(a), constant(b)) if b != 0:
		# return a % b
	
	# (multI(a, X), constant(b)):
		# d = gcd(a, b);
		# return multI(d, mod(multI((a % b) // d, X), b // d));
	
	# (constant(a), multI(b, X)):
		# d = gcd(a, b);
		# return multI(d, mod(a // d, multI(b // d, X)));
	
	# (multI(a, X), multI(b, Y)):
		# d = gcd(a, b);
		# return multI(d, mod(multI((a % b) // d, X), multI(b // d, X)));
	
	# default:
		# return mod(lvn, rvn);

