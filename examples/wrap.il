# vim: set noai ts=8 sw=8:
.data
.text
	.frame	test, 0, %vr4
		loadI	0		=> %vr5
		sub	%vr5,	%vr4	=> %vr6
		loadI	4294901760	=> %vr7
		mult	%vr4,	%vr7	=> %vr8
		loadI	65535		=> %vr9
		mult	%vr4,	%vr9	=> %vr10
		add	%vr8,	%vr10	=> %vr11
		sub	%vr6,	%vr11	=> %vr12
		iwrite	%vr12
		ret
	.frame main, 0
		loadI 42 => %vr4
		call test, %vr4

