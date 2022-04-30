.data

.text
.frame pre_example, 4, %vr5, %vr6, %vr7
		loadI 4 => %vr8
		i2i %vr8 => %vr9
		loadI 5 => %vr10
		comp %vr5, %vr10 => %vr11
		testge %vr11 => %vr12
		cbr %vr12 -> .L1
	.L0: nop
		add %vr6, %vr9 => %vr13
		load %vr7 => %vr14
		store %vr13 => %vr7
		loadI 1 => %vr16
		add %vr5, %vr16 => %vr17
		i2i %vr17 => %vr5
		loadI 5 => %vr10
		comp %vr5, %vr10 => %vr11
		testge %vr11 => %vr12
		cbrne %vr12 -> .L0
	.L1: nop
		load %vr7 => %vr14
		iwrite %vr14
		ret

.frame main, 4 
	loadI 0 => %vr18
	i2i %vr18 => %vr19
	loadI 3 => %vr20
	loadI 2 => %vr21
	i2i %vr0 => %vr22
	loadI 0 => %vr18
	sub %vr22, %vr18 => %vr23
	store %vr19 => %vr23
	call pre_example, %vr20, %vr21, %vr23
	ret


