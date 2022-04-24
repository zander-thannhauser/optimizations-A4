.data

.text
.frame main, 12 
    loadI 0 => %vr5
    i2i %vr5 => %vr6
    loadI 5 => %vr7
    i2i %vr7 => %vr8
    loadI 3 => %vr9
    i2i %vr9 => %vr10
    loadI 3 => %vr9
    comp %vr8, %vr9 => %vr11
    testle %vr11 => %vr12
    cbr %vr12 -> .L0
    add %vr8, %vr10 => %vr13
    i2i %vr13 => %vr6
    jumpI -> .L1
.L0: nop
    add %vr8, %vr10 => %vr13
    i2i %vr13 => %vr6
    jumpI -> .L1
.L2: nop
.L1: nop
    add %vr8, %vr10 => %vr13
    i2i %vr13 => %vr6
    iwrite %vr6
    ret
