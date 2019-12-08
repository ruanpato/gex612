.data
isntTri:    .string "Isn't A Triangle\n"
isTrian:    .string "Is A Triangle\n"
.text
    addi    a0, zero, 4         # a0 == a = 4
    addi    a1, zero, 4         # a1 == b = 4 // Ex: If change this to 3 isn't a triangle
    addi    a2, zero, 8         # a2 == c = 8
    jal     Bigger              # Call function Bigger

    jal     IsTriangle          # Call Function IsTriangle

    li      a7, 10              # Exit code loaded in a7
    ecall                       # Ecall to finish execution

# Arguments: a0(int), a1(int), a2(int)
# Returns: s0 = Bigger(a0, a1, a2), s1 = sum(!Bigger(a0, a1, a2))
Bigger:
    add     s0, a0, zero            # s0 = a0
    bgt     a1, s0, a1_bigger       # if a1 > a0 then a1_bigger
    bgt     a2, s0, a2_bigger       # if a2 > a0 then a2_bigger
    add     s1, a1, a2              # if a0 is the bigger, s1 = a1+a2
    ret                             # if a0 is the bigger value

    a1_bigger:                      # if(a1 > a0)
        add     s0, a1, zero        # s0 = a1
        blt     a2, a1, a2_bigger   # if (a2 > a1) then a2_bigger
        add     s1, a0, a2          # if a2 is the bigger value, s1 = a0+a2
        ret                         # if a1 is the bigger value

    a2_bigger:
        add     s0, a2, zero        # if(a2 > a1 > a0)
        add     s1, a0, a1          # if a2 is the bigger value, s1 = a0+a1
        ret

# Arguments: s0(int), s1(int)
# Returns: N/A
IsTriangle:
    bgt     s0, s1, IsntTriangle    # If X > y+z (when X is the bigger value)
    la      a0, isTrian             # Load string address
    li      a7, 4                   # Print String code
    ecall                           # Ecall to print string
    ret
    IsntTriangle:
        la      a0, isntTri         # Load string address
        li      a7, 4               # Print String code
        ecall                       # Ecall to print string
        ret