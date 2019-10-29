# Just to start #
.data
    str1: .string "Digite o número p/ fibonacci: "
    str2: .string "O valor de "
    str3: .string " fibonnaci é "
    str4: .string ".\n"
    str5: .string "1) Para calcular o fibonacci de outro número.\n0) Para encerrar a execução.\n-> "
.text
# -------------------- Function main -------------------- #
#                     Arguments: N/A                      #
#           Registers in use: a0, a7, s0, zero            #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
main:
    la      a0, str1                                      # a0 receive address of str1
    li      a7, 4                                         # Enviroment Call loaded in a7 to print string
    ecall                                                 # Ecall

    li      a7, 5                                         # Enviroment Call to read integer
    ecall                                                 # Ecall

    add     s0, a0, zero                                  # Save the value Read in s0
    jal     fibonacci                                     # Jump to Fibonacci and link at this point in ra
    add     s1, a1, zero                                  # Save de calculate fibonacci value in s1

# Printing Fibonacci result:
    la      a0, str2                                      # a0 receive address of str2
    li      a7, 4                                         # Enviroment Call loaded in a7 to print string
    ecall                                                 # Ecall

    # a1 is the int
    li      a7, 1                                         # Enviroment Call loaded in a7 to print integer
    add     a0, s0, zero                                  # s0 is the value who is solicited factorial
    ecall                                                 # Ecall

    la      a0, str3                                      # a0 receive address of str3
    li      a7, 4                                         # Enviroment Call loaded in a7 to print string
    ecall                                                 # Ecall

    li      a7, 1                                         # Enviroment Call loaded in a7 to print integer
    add     a0, s1, zero                                  # a1 is the calculated s0 factorial
    ecall                                                 # Ecall

    la      a0, str4                                      # a0 receive address of str4
    li      a7, 4                                         # Enviroment Call loaded in a7 to print string
    ecall                                                 # Ecall

    la      a0, str5                                      # a0 receive address of str5
    li      a7, 4                                         # Enviroment Call loaded in a7 to print string
    ecall                                                 # Ecall

    li      a7, 5                                         # Enviroment Call to read integer
    ecall                                                 # Ecall

    bne     a0, zero, main                                # Goes to begin of code

    j       exit                                          # Exit
# ----------------- Function fibonacci ------------------ #
#                     Arguments: a0                       #
#           Registers in use:           #
#                      Returns: a1                        #
#                     Comments: N/A                       #
#          Restrictions: Need be called using jal         #
fibonacci:
    # return ( fibonacci(n-1) + fibonnaci(n-2) )
    slti    t0, a0, 2                                     # Verify if a0 < 2
    beq     t0, zero, fib_recursion                       # Goes to fib_recursion if t0 == 0
    add     a1, zero, a0                                  # Return a0 if a0 < 2
    jr      ra                                            # Returns to register address value
    fib_recursion:
        addi    sp, sp, -12                               # Allocate three spaces in stack(4 for each)
        sw      ra, 0(sp)                                 # Store register address
        sw      a0, 4(sp)                                 # Store a0 value
        # fibonnaci(n-2)
        addi    a0, a0, -2                                # Second case of recursion
        jal     fibonacci                                 # Call recursion

        lw      a0, 4(sp)                                 # Restore a0 value from stack
        sw      a1, 8(sp)                                 # Save accumulate value of return

        # fibonnaci(n-1)
        addi    a0, a0, -1                                # First case of recursion
        jal     fibonacci                                 # Call recursion

        lw      ra, 0(sp)                                 # get's Return value
        lw      t0, 8(sp)                                 # 

        addi    sp, sp, 12                                #
        add     a1, a1, t0                                # Sum accumulates of recursion cases
        jr      ra                                        # Return to ra

# ------------------- Function exit --------------------- #
#                    Arguments: N/A                       #
#                 Registers in use: a7                    #
#                     Returns: N/A                        #
#                    Comments: N/A                        #
#                  Restrictions: N/A                      #
exit:
    li      a7, 93                                        # Enviroment Call loaded in a7 to exit program
    ecall                                                 # Ecall