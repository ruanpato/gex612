# Just to start #
.data

.text
# ------------ Função main ------------ #
#        Registradores em uso: s0       #
main:
    addi    s0, zero, 1                             # Inicia o s0, com 1
    jal     fatorial                                # Chama fatorial
    addi    a0, a1, 0                               # Número a ser printado
    addi    a7, zero, 1                             # Identificador da chamada de print integer
    ecall

# ---------- Função fatorial ---------- #
#       Registrador de entrada: a0      #
#   Registradores em uso: sp, t0, t1    #
#       Registrador de retorno: a1      #
fatorial:
    slti        t0, a0, 2                           # t0 = a0 < 2 ? 1 : 0
    beqi        t0, 1, menor_que_2                  # Chama menor que 2
    j           multiplica_decrementa               # Multiplica e decrementa

    menor_que_2:
        add         a1, s0, zero                    # a1 é valor de retorno
        #lw          ra, 0(sp)                       # ra = topo do stack pointer
        #addi        sp, sp -4                       # Decrementa o stack pointer
        addi        a1, s0, 0                       # a1 é a variável de retorno
        jr          ra                              # Retorna

    multiplica_decrementa:
        mul         s0, s0, a0                      # s0 *= a0
        addi        a0, a0, -1                      # a0--
        j           fatorial                        # chama fatorial novamente