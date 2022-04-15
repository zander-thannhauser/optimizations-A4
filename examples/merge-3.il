# vim: set noai ts=8 sw=8:

.data

.text
.frame main, 42, %vr4, %vr5
	cbr %vr4 -> .L2
	.L1:
		loadI 2 => %vr6
		i2i %vr6 => %vr7
		jumpI -> .L3
	.L2:
		cbr %vr5 -> .L22
		.L21:
			loadI 3 => %vr6
			i2i %vr6 => %vr7
			jumpI -> .L3
		.L22:
			loadI 4 => %vr6
			i2i %vr6 => %vr7
	.L3:
		iwrite %vr7
	ret
