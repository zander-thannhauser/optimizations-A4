
from debug import *;

def multiplicity_union(a, b):
	enter(f"multiplicity_union(a = {a}, b = {b}))");
	
	c = [];
	
	i, n = 0, len(a);
	j, m = 0, len(b);
	
	while i < n and j < m:
		A = a[i];
		B = b[j];
		if A[0] < B[0]:
			c.append(A); i = i + 1;
		elif A[0] > B[0]:
			c.append(B); j = j + 1;
		else:
			c.append((B[0], A[1] + B[1]));
			i = i + 1;
			j = j + 1;
	
	c += a[i:] + b[j:];
	
	exit(f"return {c};");
	return c;

