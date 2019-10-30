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
    add     s0, a0, zero
    add     s1, a0, zero
    jal     until_k
    #add     t6, a0, zero  # t6 = n
    
    #li      a7, 5
    #ecall

    #add     a1, a0, zero    # a1 = k
    #add     a0, t6, zero    # a0 = t6
    #jal     ST_2

    #add     s0, a0, zero                                    # n
    #add     s1, a0, zero                                    # k
    #jal     until_k                                         #

    mv      a0, a2
    li      a7, 1
    ecall
    la      a0, str2                                  # Carrega o endereço de str0 em a0
    li      a7, 4                                     # 4 é a "Enviroment Call" que faz "impressão" de "string"
    ecall                                             # Realiza ecall


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
#                      Returns: a2                        #
#                     Comments: N/A                       #
# int ST_2(int n, int k){
##    if(k==0)
#        return 0;
##    if(n > 1)
#        return k * ST_2(n-1, k) + ST_2(n-1, k-1);
##    if(k > 1)
#        return 0;
#    return 1;
#}
ST_2:
    ## if(n<0)
    slt     t4, a0, zero
    bne     t4, zero, ST_2_k_0
    ## if(k<0)
    slt     t4, a1, zero
    bne     t4, zero, ST_2_k_0
    ## if(n==k)
    beq     a0, a1, ST_2_k_1                              # if (n==k)
    ## if(k==0)
    beq     a1, zero, ST_2_k_0                            # if(k==0)
    ## if(n>1)
    li      t4, 1                                         # t4 = 1
    slt     t5, t4, a0                                    # if(1 < n) t5 = 1 else t5 = 0
    bne     t5, zero, ST_2_recursion                      # if(n > 1) return k * ST_2(n-1, k)+ST_2(n-1, k-1)
    ## if(k>1)
    li      t4, 1                                         # t4 = 1
    slt     t5, t4, a1                                    # if(1 < k) t5 = 1 else t5 = 0
    bne     t5, zero, ST_2_k_0                            # if(k > 1) return 0

    j       ST_2_k_1                                      # Return 1

    ST_2_recursion:
        addi    sp, sp, -16                               # Aloca espaço na pilha
        sw      ra, 0(sp)                                 # Aloca endereço de retorno na primeira posição da pilha
        sw      s5, 4(sp)                                 # Aloca o 'resultado' na segunda posição pilha
        sw      a0, 8(sp)                                 # Aloca o n na terceira posição da pilha
        sw      a1, 12(sp)                                # Aloca o k na quarta posição da pilha

        # ST_2(n-1, k)
        addi    a0, a0, -1                                # n = n-1
        jal     ST_2                                      # recursive call
        mul     s5, a0, a2                                # s5* = n*ST_2(n-1, k)
        #lw      a0, 8(sp)                                # Recupera o valor de n
        sw      s5, 4(sp)                                 # Salva o acumulado em s5

        # ST_2(n-1, k-1)
        lw      a0, 8(sp)                                 # Recupera o valor a da pilha
        addi    a0, a0, -1                                # a0 = n-1
        addi    a1, a1, -1                                # a1 = k-1

        jal     ST_2                                      # "Chamada recursiva"
        lw      s5, 4(sp)                                 # Recupera o acumulado
        add     s5, s5, a2                                # s5 = k*ST_2(n-1, k)+ST_2(n-1, k-1)
        sw      s5, 4(sp)                                 # Devolve o "total" pra pilha
        add     a2, s5, zero                              # Coloca o acumulado em a2

        lw      ra, 0(sp)
        addi    sp, sp, 16
        jr      ra
    
    ST_2_k_0:
        li      a2, 0                                     # Carrega no registrador de retorno o valor zero
        jr      ra                                        # Retorna pra onde foi chamado

    ST_2_k_1:
        li      a2, 1                                     # Carrega no registrador de retorno o valor zero
        jr      ra                                        # Retorna pra onde foi chamado
# ------------------ Function: until_k ------------------ #
#                 Arguments: s0(n), s1(k)                 #
#           Registers in use:             #
#                      Returns: N/A                       #
#                     Comments: N/A                       #
until_k:
    li      t1, 1                                         # t1 = 1
    beq     s1, t1, return_until_k                        # if (k == 1)

    add     a0, s0, zero                                  # a0 = n
    add     a1, s1, zero                                  # a1 = k
    jal     ST_2                                          #

    add     a0, a2, zero
    li      a7, 1                                     # 1 é a "Enviroment Call" que "imprime" um "inteiro"
    ecall                                             # Realiza ecall

    la      a0, str1                                      # Carrega o endereço de str1 em a0
    li      a7, 4                                         # 4 é a "Enviroment Call" que faz "impressão" de "string"
    ecall                                                 # Realiza ecall

    addi    s1, s1, -1                                    # k--
    j       until_k                                       # Volta pro until_k

    return_until_k:
        add     a0, s0, zero                              # a0 = n
        add     a1, s1, zero                              # a1 = k
        jal     ST_2                                      #

        add     a0, a2, zero

        li      a7, 1                                     # 1 é a "Enviroment Call" que "imprime" um "inteiro"
        ecall                                             # Realiza ecall

        la      a0, str2                                  # Carrega o endereço de str0 em a0
        li      a7, 4                                     # 4 é a "Enviroment Call" que faz "impressão" de "string"
        ecall                                             # Realiza ecall

        j        exit
        #jr      ra                                        # Retorna para registrador origem