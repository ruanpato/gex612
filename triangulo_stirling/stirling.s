## Autores: Ruan Natan Guerra Pato   ##
## 

.data
str0:       .string "Digite um valor k: "
str1:       .string ", "
str2:       .string ".\n"
.text

# ------------------- Function: main -------------------- #
#                     Arguments: N/A                      #
#           Registers in use:             #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
main:
    la      a0, str0                                      # Carrega o endereço de str0 em a0
    li      a7, 4                                         # 4 é a "Enviroment Call" que faz "impressão" de "string"
    ecall                                                 # Realiza ecall

    li      a7, 5                                         # 4 é a "Enviroment Call" que faz "leitura" de "inteiro"
    ecall                                                 # Realiza ecall

    mv      s0, a0                                        #
    mv      s2, a0                                        # 
    jal     until_k                                       #

    j       exit                                          # Vai para exit

# -------------------- Function: exit ------------------- #
#                     Arguments: N/A                      #
#           Registers in use:             #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
exit:
    li      a7, 93                                        # 93 é a "Enviroment Call" para encerrar execução
    ecall                                                 # Realiza ecall
# ------------------- Function: ST_2 -------------------- #
#                 Arguments: a0(n), a1(k)                 #
#           Registers in use:             #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
ST_2:
    addi    sp, sp, -16                                   # Aloca espaço na pilha
    sw      ra, 0(sp)                                     # Aloca endereço de retorno na primeira posição da pilha
    sw      s3, 4(sp)                                     # Aloca o 'resultado' na pilha
    bne     a1, zero, ST_2_recursion                      # S2 k != 0
    addi    a1, zero, 1                                   # a1 recebe 1

    j       ST_2_return                                   # Retorna o valor calculado

    ST_2_recursion:
        mv      s1, a0                                    # s1 := a0
        addi    a0, a0, -1                                # n=n-1
        jal     ST_2                                      # recursive call
        mul     a1, s1, a1                                # a1 = n*n-1

        lw      a0, 4(sp)                                 # Restore a0 value from stack
        sw      a1, 8(sp)                                 # Save accumulate value of return

    ST_2_return:
        lw      s1, 4(sp)                                 # Load aux register
        lw      ra, 0(sp)                                 # Return address
        addi    sp, sp, 12                                # Decrement stack
        jr      ra                                        # Return to register address position
# ------------------ Function: until_k ------------------ #
#                     Arguments: s0                       #
#           Registers in use:             #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
until_k:
    li      s1, 1                                         #
    beq     s0, s1, return_until_k                        #

    mv      a0, s0                                        #
    #jal    ST_2                                           #
    li      a7, 1                                         # 1 é a "Enviroment Call" que "imprime" um "inteiro"
    ecall                                                 # Realiza ecall

    la      a0, str1                                      # Carrega o endereço de str0 em a0
    li      a7, 4                                         # 4 é a "Enviroment Call" que faz "impressão" de "string"
    ecall                                                 # Realiza ecall


    li      a0, -1                                        # Helper to 64bits
    add     s0, s0, a0                                    # 
    j       until_k                                       # Volta pro until_k

    return_until_k:

        mv      a0, s0                                    #
        #jal    ST_2                                       #

        li      a7, 1                                     # 1 é a "Enviroment Call" que "imprime" um "inteiro"
        ecall                                             # Realiza ecall

        la      a0, str2                                  # Carrega o endereço de str0 em a0
        li      a7, 4                                     # 4 é a "Enviroment Call" que faz "impressão" de "string"
        ecall                                             # Realiza ecall

        jr      ra                                        # Retorna para registrador origem