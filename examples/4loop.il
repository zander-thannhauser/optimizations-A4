.data

.text
.frame main, 16 
    loadI 0 => %vr5
    i2i %vr5 => %vr6
    loadI 10 => %vr7
    comp %vr6, %vr7 => %vr8
    testgt %vr8 => %vr9
    cbr %vr9 -> .L1
.L0: nop
    loadI 0 => %vr5
    i2i %vr5 => %vr10
    loadI 10 => %vr7
    comp %vr10, %vr7 => %vr11
    testgt %vr11 => %vr12
    cbr %vr12 -> .L3
.L2: nop
    loadI 0 => %vr5
    i2i %vr5 => %vr13
    loadI 10 => %vr7
    comp %vr13, %vr7 => %vr14
    testgt %vr14 => %vr15
    cbr %vr15 -> .L5
.L4: nop
    loadI 0 => %vr5
    i2i %vr5 => %vr16
    loadI 10 => %vr7
    comp %vr16, %vr7 => %vr17
    testgt %vr17 => %vr18
    cbr %vr18 -> .L7
.L6: nop
    add %vr16, %vr6 => %vr19
    add %vr19, %vr13 => %vr20
    add %vr20, %vr6 => %vr21
    add %vr21, %vr10 => %vr22
    add %vr22, %vr6 => %vr23
    iwrite %vr23
    loadI 1 => %vr24
    add %vr16, %vr24 => %vr25
    i2i %vr25 => %vr16
    loadI 10 => %vr7
    comp %vr16, %vr7 => %vr17
    testgt %vr17 => %vr18
    cbrne %vr18 -> .L6
.L7: nop
    loadI 1 => %vr24
    add %vr13, %vr24 => %vr26
    i2i %vr26 => %vr13
    loadI 10 => %vr7
    comp %vr13, %vr7 => %vr14
    testgt %vr14 => %vr15
    cbrne %vr15 -> .L4
.L5: nop
    loadI 1 => %vr24
    add %vr10, %vr24 => %vr27
    i2i %vr27 => %vr10
    loadI 10 => %vr7
    comp %vr10, %vr7 => %vr11
    testgt %vr11 => %vr12
    cbrne %vr12 -> .L2
.L3: nop
    loadI 1 => %vr24
    add %vr6, %vr24 => %vr28
    i2i %vr28 => %vr6
    loadI 10 => %vr7
    comp %vr6, %vr7 => %vr8
    testgt %vr8 => %vr9
    cbrne %vr9 -> .L0
.L1: nop
    ret
