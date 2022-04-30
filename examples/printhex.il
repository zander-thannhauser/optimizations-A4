.data

.text
.frame printhex_recursive, 4, %vr5
    loadI 16 => %vr6
    mod %vr5, %vr6 => %vr7
    i2i %vr7 => %vr8
    loadI 16 => %vr6
    comp %vr5, %vr6 => %vr9
    testlt %vr9 => %vr10
    cbr %vr10 -> .L1
    loadI 4 => %vr11
    rshift %vr5, %vr11 => %vr12
    call printhex_recursive, %vr12
.L1: nop
    loadI 10 => %vr13
    comp %vr8, %vr13 => %vr14
    testge %vr14 => %vr15
    cbr %vr15 -> .L2
    loadI 48 => %vr16
    add %vr16, %vr8 => %vr17
    putchar %vr17
    jumpI -> .L3
.L2: nop
    loadI 65 => %vr18
    loadI 10 => %vr13
    sub %vr8, %vr13 => %vr19
    add %vr18, %vr19 => %vr20
    putchar %vr20
    jumpI -> .L3
.L4: nop
.L3: nop
    ret
.frame printhex, 0, %vr5
    call printhex_recursive, %vr5
    loadI 10 => %vr13
    putchar %vr13
    ret
.frame main, 4 
    loadI 0 => %vr21
    i2i %vr21 => %vr5
    i2i %vr0 => %vr22
    loadI 0 => %vr21
    sub %vr22, %vr21 => %vr23
    store %vr5 => %vr23
    iread %vr23
    load %vr23 => %vr24
    call printhex, %vr24
    ret
