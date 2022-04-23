
.data
	.string .test, "4321"

.text
.frame main, 0
	loadI .test => %vr4
	loadAI  %vr4, 1 => %vr5
	loadAI  %vr4, 2 => %vr6
	storeAI %vr6 => %vr4, 1
	storeAI %vr5 => %vr4, 2
	swrite %vr4
	ret
