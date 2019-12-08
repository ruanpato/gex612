.data

.text
main:
    addi    a0, zero, 5         # a0 == a = 5
    addi    a1, zero, 4         # a1 == b = 4
    jal     multiplica          # multiplica(a, b)

    li      a7, 10              # Exit code loaded in a7
    ecall                       # Ecall to finish execution

# Arguments: a0(int), a1(int)
# Returns: s0 = a0*a1
multiplica:
    add     s0, zero, zero      # s0 == ans = 0
    add     t0, zero, zero      # t0 == i = 0
    j       loop_multiplica     # loop_multiplica(a1), [a1==n]

    loop_multiplica:                        # for(i=0; i < n; i++)
        add     s0, s0, a0                  # s0 += a0
        addi    t0, t0, 1                   # i++
        blt     t0, a1, loop_multiplica     # if (i < n)
        ret                                 # s0 has the multiplied value