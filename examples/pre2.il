.data
    .string .str_const_0, "howdy"
.text
.frame main, 16 
    loadI 0 => %vr5
    i2i %vr5 => %vr6
    loadI 0 => %vr5
    i2i %vr5 => %vr7
    i2i %vr0 => %vr9
    loadI 4 => %vr8
    sub %vr9, %vr8 => %vr10
    store %vr7 => %vr10
    iread %vr10
    loadI 3 => %vr11
    i2i %vr11 => %vr12
    load %vr10 => %vr13
    loadI 3 => %vr11
    comp %vr13, %vr11 => %vr14
    testle %vr14 => %vr15
    cbr %vr15 -> .L0
    load %vr10 => %vr13
    load %vr10 => %vr13
    add %vr13, %vr13 => %vr16
    i2i %vr16 => %vr17
    load %vr10 => %vr13
    add %vr13, %vr12 => %vr18
    i2i %vr18 => %vr6
    iwrite %vr17
    jumpI -> .L1
.L0: nop
    load %vr10 => %vr13
    add %vr13, %vr12 => %vr18
    i2i %vr18 => %vr6
    loadI .str_const_0 => %vr19
    swrite %vr19
    jumpI -> .L1
.L2: nop
.L1: nop
    iwrite %vr6
    ret
