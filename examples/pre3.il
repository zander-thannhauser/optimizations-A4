.data

.text
.frame pre_example, 4, %vr5, %vr6, %vr7
    loadI 0 => %vr8
    i2i %vr8 => %vr9
    loadI 5 => %vr10
    comp %vr9, %vr10 => %vr11
    testge %vr11 => %vr12
    cbr %vr12 -> .L1
.L0: nop
    add %vr5, %vr6 => %vr13
    i2i %vr13 => %vr7
    loadI 1 => %vr14
    add %vr9, %vr14 => %vr15
    i2i %vr15 => %vr9
    loadI 5 => %vr10
    comp %vr9, %vr10 => %vr11
    testge %vr11 => %vr12
    cbrne %vr12 -> .L0
.L1: nop
    iwrite %vr7
    ret
.frame main, 0 
    loadI 3 => %vr16
    loadI 1 => %vr14
    loadI 2 => %vr17
    call pre_example, %vr16, %vr14, %vr17
    ret
