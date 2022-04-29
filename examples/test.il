# vim: set noai ts=8 sw=8:
	.data
	.string	.int_wformat, "%d\12"
	.string	.float_wformat, "%f\12"
	.string	.char_wformat, "%c\12"
	.string	.string_wformat, "%s\12"
	.string	.int_rformat, "%d"
	.string	.float_rformat, "%f"
	.string	.char_rformat, "%c"
	.string	.string_rformat, "%s"
	.string	.string_const_0, "A?"
	.string	.string_const_1, "A:"
	.float	.float_const_0, 1.7
	.global	main_fp, 4, 4
.text
	.frame	partition, 0, %vr4, %vr5, %vr6
		load	%vr5  => %vr12
		loadI	0  => %vr13
		sub	%vr12, %vr13 => %vr14
		loadI	4  => %vr15
		mult	%vr14, %vr15 => %vr16
		sub	%vr4, %vr16 => %vr17
		load	%vr17  => %vr18
		i2i	%vr18  => %vr9
		load	%vr5  => %vr12
		loadI	1  => %vr19
		sub	%vr12, %vr19 => %vr20
		i2i	%vr20  => %vr7
		load	%vr6  => %vr21
		loadI	1  => %vr19
		add	%vr21, %vr19 => %vr22
		i2i	%vr22  => %vr8
		loadI	.float_const_0  => %vr23
		fload	%vr23  => %vr24
		f2i	%vr24  => %vr25
		loadI	0  => %vr13
		comp	%vr25, %vr13 => %vr26
		testeq	%vr26  => %vr27
		cbr	%vr27  -> .L4
	.L5:	nop
		loadI	1  => %vr19
		sub	%vr8, %vr19 => %vr28
		i2i	%vr28  => %vr8
		loadI	0  => %vr13
		sub	%vr8, %vr13 => %vr29
		loadI	4  => %vr15
		mult	%vr29, %vr15 => %vr30
		sub	%vr4, %vr30 => %vr31
		load	%vr31  => %vr32
		comp	%vr32, %vr9 => %vr33
		testle	%vr33  => %vr34
		cbr	%vr34  -> .L6
	.L7:	nop
		loadI	1  => %vr19
		sub	%vr8, %vr19 => %vr28
		i2i	%vr28  => %vr8
		loadI	0  => %vr13
		sub	%vr8, %vr13 => %vr29
		loadI	4  => %vr15
		mult	%vr29, %vr15 => %vr30
		sub	%vr4, %vr30 => %vr31
		load	%vr31  => %vr32
		comp	%vr32, %vr9 => %vr33
		testgt	%vr33  => %vr34
		cbr	%vr34  -> .L7
	.L6:	nop
		loadI	1  => %vr19
		add	%vr7, %vr19 => %vr35
		i2i	%vr35  => %vr7
		loadI	0  => %vr13
		sub	%vr7, %vr13 => %vr36
		loadI	4  => %vr15
		mult	%vr36, %vr15 => %vr37
		sub	%vr4, %vr37 => %vr38
		load	%vr38  => %vr39
		comp	%vr39, %vr9 => %vr40
		testge	%vr40  => %vr41
		cbr	%vr41  -> .L8
	.L9:	nop
		loadI	1  => %vr19
		add	%vr7, %vr19 => %vr35
		i2i	%vr35  => %vr7
		loadI	0  => %vr13
		sub	%vr7, %vr13 => %vr36
		loadI	4  => %vr15
		mult	%vr36, %vr15 => %vr37
		sub	%vr4, %vr37 => %vr38
		load	%vr38  => %vr39
		comp	%vr39, %vr9 => %vr40
		testlt	%vr40  => %vr41
		cbr	%vr41  -> .L9
	.L8:	nop
		comp	%vr7, %vr8 => %vr42
		testlt	%vr42  => %vr43
		cbrne	%vr43  -> .L10
		loadI	0  => %vr13
		sub	%vr7, %vr13 => %vr36
		loadI	4  => %vr15
		mult	%vr36, %vr15 => %vr37
		sub	%vr4, %vr37 => %vr38
		load	%vr38  => %vr39
		i2i	%vr39  => %vr10
		loadI	0  => %vr13
		sub	%vr8, %vr13 => %vr29
		loadI	4  => %vr15
		mult	%vr29, %vr15 => %vr30
		sub	%vr4, %vr30 => %vr31
		load	%vr31  => %vr32
		loadI	0  => %vr13
		sub	%vr7, %vr13 => %vr36
		loadI	4  => %vr15
		mult	%vr36, %vr15 => %vr37
		sub	%vr4, %vr37 => %vr38
		store	%vr32  => %vr38
		loadI	0  => %vr13
		sub	%vr8, %vr13 => %vr29
		loadI	4  => %vr15
		mult	%vr29, %vr15 => %vr30
		sub	%vr4, %vr30 => %vr31
		store	%vr10  => %vr31
		jumpI	-> .L11
	.L10:	nop
		iret	%vr8
	.L11:	nop
		loadI	.float_const_0  => %vr23
		fload	%vr23  => %vr24
		f2i	%vr24  => %vr25
		cbr	%vr25  -> .L5
	.L4:	nop
		ret
