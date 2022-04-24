.data

.text
.frame test, 0, %vr5, %vr6
    loadI 0 => %vr7
    comp %vr6, %vr7 => %vr8
    testeq %vr8 => %vr9
    cbr %vr9 -> .L0
    loadI 2 => %vr10
    add %vr5, %vr10 => %vr11
    iwrite %vr11
    jumpI -> .L1
.L0: nop
    loadI 2 => %vr10
    add %vr5, %vr10 => %vr11
    i2i %vr11 => %vr6
    jumpI -> .L1
.L2: nop
.L1: nop
    loadI 2 => %vr10
    add %vr5, %vr10 => %vr11
    iwrite %vr11
    ret
.frame main, 0 
    loadI 2 => %vr10
    loadI 3 => %vr12
    call test, %vr10, %vr12
    ret
