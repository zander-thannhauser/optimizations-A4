.data

.text
.frame main, 4 
    loadI 0 => %vr5
    i2i %vr5 => %vr6
    loadI 7 => %vr7
    add %vr7, %vr6 => %vr8
    loadI 5 => %vr9
    sub %vr8, %vr9 => %vr10
    iwrite %vr10
    loadI 10 => %vr11
    comp %vr6, %vr11 => %vr12
    testge %vr12 => %vr13
    cbr %vr13 -> .L1
.L0: nop
    loadI 2 => %vr14
    loadI 1 => %vr15
    add %vr6, %vr15 => %vr16
    mult %vr14, %vr16 => %vr17
    sub %vr17, %vr6 => %vr18
    iwrite %vr18
    loadI 10 => %vr11
    i2i %vr11 => %vr6
    loadI 10 => %vr11
    comp %vr6, %vr11 => %vr12
    testge %vr12 => %vr13
    cbrne %vr13 -> .L0
.L1: nop
    ret
