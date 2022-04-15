# vim: set noai ts=8 sw=8:

.data
.string .string_const_0, "Hello world!"

.text
.frame main, 42
	loadI .string_const_0 => %vr4
	swrite %vr4
	ret
