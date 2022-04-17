.data

.text

.frame test, 0, a, b, c, d
	
	add a,   b => apb   # a + b = apb
	add apb, c => apbpc # (a + b) + c = apbpc
	add c,   b => cpb   # c + b = cpb
	add cpb, a => cpbpa # (c + b) + a = cpbpa
	
	# a + b + c == c + b + a
	comp apbpc, cpbpa => t1
	testeq t1 => t2
	assert t2
	
	# (a + b + c) - a == b + c
	sub apbpc, a => t1
	comp cpb, t1 => t2
	testeq t2 => t3
	assert t3
	
	add cpb, d => cpbpd # c + b + d = cbd
	sub a,   d => amd   # a - d = amd
	
	# (a + b + c) - (c + b + d) == a - d;
	sub apbpc, cpbpd => t1
	comp t1, amd => t2
	testeq t2 => t3
	assert t3
	
	mult a,   b => atb   # a   * b = atb
	mult atb, c => atbtc # atb * c = atbtc
	mult c,   b => ctb   # c   * b = ctb
	mult ctb, a => ctbta # ctb * a = ctbta
	
	# a * b * c == c * b * a
	comp atbtc, ctbta => t1
	testeq t1 => t2
	assert t2
	
	mult ctb, d => ctbtd # cb * d = cbd
	add  a,   d => apd # a + d
	
	# (a * b * c) + (c * b * d) == b * c * (a + d)
	add atbtc, ctbtd => t1
	mult ctb, apd => t2
	comp t1, t2 => t3
	testeq t3 => t4
	assert t4
	
	loadI 1 => o
	
	# (a * (a + 1) * b) + ((a + 1) * b) == ((a + 1) ^ 2 * b)
	add    a,   o   => ap1 # a + 1
	mult   atb, ap1 => t1  # (a * b) * (a + 1)
	mult   ap1, b   => t2  # (a + 1) * b
	add    t1,  t2  => t3  # (a * b) * (a + 1) + (a + 1) * b
	mult   ap1, ap1 => t4  # (a + 1) * (a + 1)
	mult   t4,  b   => t5  # (a + 1) * (a + 1) * b
	comp   t3,  t5  => t6
	testeq t6       => t7
	assert t7
	
	sub a, d => amd # a - d
	
	# (a * b * c) - (c * b * d) == b * c * (a - d)
	sub atbtc, ctbtd => t1
	mult ctb, amd => t2
	comp t1, t2 => t3
	testeq t3 => t4
	assert t4
	
	loadI 0 => z
	
	# (a * b * c) % (c * b * a) == 0
	mod atbtc, ctbta => t1
	comp t1, z => t2
	testeq t2 => t3
	assert t3

	mod a, d => avd # a % d
	
	# (a * b * c) % (c * b * d) == (b * c * (a % d))
	mod  atbtc, ctbtd => t1
	mult avd, ctb => t2
	comp t1, t2 => t3
	testeq t3 => t4
	assert t4
	
	# (a * b * c) % (a * b) == a * b * (c % 1))
	mod  atbtc, atb => t1
	mod  c, o => t2
	mult atb, t2 => t3
	comp t1, t3 => t4
	testeq t4 => t5
	assert t5
	

.frame main, 0
	call test 1 2 3 4
	ret






















