
.data
.text
.frame pre_example, 4, %vr100, %vr200, %vr300
	loadI 4 => %vr4
	i2i %vr4 => %vr5
	loadI 5 => %vr6
	comp %vr100, %vr6 => %vr7
	testge %vr7 => %vr8
	cbr %vr8 -> .L1

.L0: nop
	add %vr200, %vr5 => %vr9
	i2i %vr9 => %vr300
	
	loadI 1 => %vr10
	add %vr100, %vr10 => %vr11
	i2i %vr11 => %vr100
	
	loadI 5 => %vr6
	comp %vr100, %vr6 => %vr7
	testge %vr7 => %vr8
	cbrne %vr8 -> .L0

.L1: nop
	iwrite %vr300
	ret

