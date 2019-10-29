# Just to start #
.data
    str1: .string "Digite o número p/ fatorial: "
    str2: .string "O valor de "
    str3: .string "! é "
    str4: .string ".\n"
    str5: .string "1) Para calcular o fatorial de outro número.\n0) Para encerrar a execução.\n-> "
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
    jal     factorial                                     # Jump to Fibonacci and link at this point in ra
    add     s1, a1, zero                                  # Save the factorial value in s1

    # Printing Fatorial result:
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

    j       exit                                          # Finish the program execution

# ----------------- Function factorial ------------------ #
#                     Arguments: a0                       #
#           Registers in use: a0, s1, a1, sp, ra          #
#                      Returns: a1                        #
#                     Comments: N/A                       #
#          Restrictions: Need be called using jal         #
factorial:
    addi     sp, sp, -8                                   # Increment Stack
    sw       s1, 4(sp)                                    # Return value
    sw       ra, 0(sp)                                    # Return address
    bne      a0, zero, fact_else                          # Goes to "else" if a0 != 0
    addi     a1, zero, 1                                  # Return value
    j        fact_return                                  # Jumps to fact_return

    fact_else:
        mv       s1, a0                                   # Copy a0 value to s1
        addi     a0, a0, -1                               # n=n-1
        jal factorial                                     # recursive call
        mul      a1, s1, a1                               # a1 = n*n-1

    fact_return:
        lw       s1, 4(sp)                                # Load aux register
        lw       ra, 0(sp)                                # Return address
        addi     sp, sp, 8                                # Decrement stack
        jr       ra                                       # Return to register address position

# ------------------- Function exit --------------------- #
#                    Arguments: N/A                       #
#                 Registers in use: a7                    #
#                     Returns: N/A                        #
#                    Comments: N/A                        #
#                  Restrictions: N/A                      #
exit:
    li      a7, 93                                        # Enviroment Call loaded in a7 to exit program
    ecall                                                 # Ecall