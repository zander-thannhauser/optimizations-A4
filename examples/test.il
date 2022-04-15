# vim: set noai ts=8 sw=8:
.data
	.float	.float_const_0, 0.01
	.global	main_fp, 4, 4
.text
	.frame	main, 44
		loadI	-4  => %vr5
		add	%vr0, %vr5 => %vr6
		loadI	1  => %vr7
		loadI	2  => %vr7
		loadI	3  => %vr7
		call	init, %vr6
		loadI	4  => %vr7
		loadI	5  => %vr7
		loadI	6  => %vr7
	ret
	.frame	init, 20, %vr8
		loadI	9  => %vr4
		loadI	1  => %vr9
		loadI	42  => %vr19
		sub	%vr4, %vr9 => %vr20
		loadI	4  => %vr21
		mult	%vr20, %vr21 => %vr22
		sub	%vr8, %vr22 => %vr23
		store	%vr19  => %vr23
	ret

