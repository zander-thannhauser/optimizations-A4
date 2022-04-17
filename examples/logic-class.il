.data

.text

.frame test, 0, a, b, c, d
	
	or a,   b => aob   #  a || b
	or aob, c => aoboc # (a || b) || c
	or c,   b => cob   #  c || b
	or cob, a => coboa # (c || b) || a
	
	# a || b || c == c || b || a
	comp aoboc, coboa => t1
	testeq t1 => t2
	assert t2
	
	and a,   b => anb   #  a && b
	and anb, c => anbnc # (a && b) && c
	and c,   b => cnb   #  c && b
	and cnb, a => cnbna # (c && b) && a
	
	# a && b && c == c && b && a
	comp anbnc, cnbna => t1
	testeq t1 => t2
	assert t2
	
	not a => na
	not b => nb
	not c => nc
	
	# !(a && b && c) == !a || !b || !c
	not anbnc => t1
	or na, nb => t2
	or t2, nc => t3
	comp t1, t3 => t4
	testeq t4 => t5
	assert t5
	
	# !(a || b || c) == !a && !b && !c
	not aoboc => t1
	and na, nb => t2
	and t2, nc => t3
	comp t1, t3 => t4
	testeq t4 => t5
	assert t5

.frame main, 0
	call test 1 2 3 4
	ret






















