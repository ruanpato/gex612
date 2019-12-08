.data

.text
main:
    addi    a0, zero, -4        # a0 = -4
    addi    a1, zero, 50        # a1 = 50
    addi    a2, zero, -2        # a2 = -2
    jal     Menor               # Call function menor

    li      a7, 10              # Exit code loaded in a7
    ecall                       # Ecall to finish execution

# Arguments: a0(int), a1(int), a2(int)
# Returns: s0 = menor(a0, a1, a2)
Menor:
    add     s0, a0, zero            # s0 = a0
    blt     a1, s0, a1_menor        # if a1 < a0 then a1_menor
    blt     a2, s0, a2_menor        # if a2 < a0 then a2_menor
    ret                             # if a0 is the lower value

    a1_menor:                       # if(a1 < a0)
        add     s0, a1, zero        # s0 = a1
        blt     a2, a1, a2_menor    # if (a2 < a1) then a2_menor
        ret                         # if a1 is the lower value

    a2_menor:
        add     s0, a2, zero        # if(a2 < a1 < a0)
        ret