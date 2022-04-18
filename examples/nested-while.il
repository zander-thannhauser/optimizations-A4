.data

.text
.frame main, 12 
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
    loadI 0 => %vr5
    i2i %vr5 => %vr14
    loadI 1 => %vr15
    add %vr15, %vr14 => %vr16
    loadI 1 => %vr15
    add %vr16, %vr15 => %vr17
    iwrite %vr17
    loadI 20 => %vr18
    comp %vr14, %vr18 => %vr19
    testge %vr19 => %vr20
    cbr %vr20 -> .L3
.L2: nop
    loadI 1 => %vr15
    add %vr14, %vr15 => %vr21
    i2i %vr21 => %vr22
    loadI 2 => %vr23
    mult %vr23, %vr14 => %vr24
    loadI 3 => %vr25
    add %vr24, %vr25 => %vr26
    sub %vr26, %vr22 => %vr27
    iwrite %vr27
    loadI 512 => %vr28
    i2i %vr28 => %vr14
    loadI 20 => %vr18
    comp %vr14, %vr18 => %vr19
    testge %vr19 => %vr20
    cbrne %vr20 -> .L2
.L3: nop
    loadI 2 => %vr23
    loadI 1 => %vr15
    add %vr6, %vr15 => %vr29
    mult %vr23, %vr29 => %vr30
    sub %vr30, %vr6 => %vr31
    iwrite %vr31
    loadI 1 => %vr15
    rshift %vr14, %vr15 => %vr32
    i2i %vr32 => %vr6
    loadI 10 => %vr11
    comp %vr6, %vr11 => %vr12
    testge %vr12 => %vr13
    cbrne %vr13 -> .L0
.L1: nop
    ret
