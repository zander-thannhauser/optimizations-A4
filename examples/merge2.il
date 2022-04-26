.data

.text
.frame merge, 4, %vr5, %vr6
    loadI 1 => %vr7
    i2i %vr7 => %vr8
    loadI 3 => %vr9
    comp %vr5, %vr9 => %vr10
    testle %vr10 => %vr11
    cbr %vr11 -> .L0
    loadI 3 => %vr9
    comp %vr6, %vr9 => %vr12
    testge %vr12 => %vr13
    cbr %vr13 -> .L2
    iwrite %vr8
    jumpI -> .L3
.L2: nop
    loadI 3 => %vr9
    i2i %vr9 => %vr8
    jumpI -> .L3
.L4: nop
.L3: nop
    iwrite %vr8
    jumpI -> .L1
.L0: nop
    loadI 3 => %vr9
    comp %vr6, %vr9 => %vr12
    testge %vr12 => %vr13
    cbr %vr13 -> .L6
    loadI 2 => %vr14
    i2i %vr14 => %vr8
    jumpI -> .L7
.L6: nop
    loadI 3 => %vr9
    i2i %vr9 => %vr8
    jumpI -> .L7
.L8: nop
.L7: nop
    iwrite %vr8
    jumpI -> .L1
.L5: nop
.L1: nop
    ret
.frame main, 0 
    loadI 4 => %vr15
    loadI 5 => %vr16
    call merge, %vr15, %vr16
    ret
