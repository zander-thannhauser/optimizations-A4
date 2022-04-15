
.data

.text
	.frame pre_example, 4, %vr1, %vr2, %vr3
		loadI 4 => %vr4
		i2i %vr4 => %vr5
		loadI 5 => %vr6
		comp %vr1, %vr6 => %vr7
		testge %vr7 => %vr8
		cbr %vr8 -> .L1
	.L0:loadI 4 => %vr4
		load %vr3 => %vr9
		store %vr4 => %vr3
		add %vr2, %vr5 => %vr11
		load %vr3 => %vr9
		store %vr11 => %vr3
		loadI 1 => %vr12
		add %vr1, %vr12 => %vr13
		i2i %vr13 => %vr1
		loadI 5 => %vr6
		comp %vr1, %vr6 => %vr7
		testge %vr7 => %vr8
		cbrne %vr8 -> .L0
	.L1:load %vr3 => %vr9
		iwrite %vr9
	ret
