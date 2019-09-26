# Just to start #
.data


.text


# ---------- Função fatorial ---------- #
#       Registrador de entrada: a0      #
#       Registradores em uso:           #
#       Registrador de retorno: a1      #
fatorial:
    slti        t0, a0, 2                           # t0 = a0 < 2 ? 1 : 0
    beqi        t0, 1, menor_que_2                  # Chama menor que 2
    j           multiplica_decrementa               # Multiplica e decrementa