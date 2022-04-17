
from debug import *;

def multiplicity_intersection(a, b):
	enter(f"multiplicity_intersection(a = {a}, b = {b}))");
	
	c = [];
	
	i, n = 0, len(a);
	j, m = 0, len(b);
	
	while i < n and j < m:
		A = a[i];
		B = b[j];
		if A[0] < B[0]:
			i = i + 1;
		elif A[0] > B[0]:
			j = j + 1;
		else:
			C = (A[0], min(A[1], B[1], key = abs));
			c.append(C);
			i = i + 1;
			j = j + 1;
	
	exit(f"return {c};");
	return c;

