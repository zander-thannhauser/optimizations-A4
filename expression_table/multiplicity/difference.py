
from debug import *;

def multiplicity_difference(a, b):
	enter(f"multiplicity_difference(a = {a}, b = {b}))");
	
	c = [];
	
	i, n = 0, len(a);
	j, m = 0, len(b);
	
	while i < n and j < m:
		A, B = a[i], b[j];
		if A[0] < B[0]:
			c.append(A);
			i = i + 1;
		elif A[0] > B[0]:
			c.append((B[0], -B[1]));
			j = j + 1;
		else:
			if A[1] - B[1]:
				c.append((A[0], A[1] - B[1]));
			i = i + 1;
			j = j + 1;
	
	c += a[i:] + [(B[0], -B[1]) for B in b[j:]];
	
	exit(f"return {c};");
	return c;

