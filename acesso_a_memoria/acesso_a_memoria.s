# Just filling the file to create #
.data               # Area of  data declaration
vetor:              .word   2, -5, 1, 7, 36, 4, -1, 0           # Aloca um vetor do tipo word
msg_new_line:       .string "\n"                                # "Cria uma msg" de quebra de linha
msg_blank_space:    .string " "                                 # "Cria uma msg" de espaço em branco
msg_vetor:          .string "Vetor:"                            # "Cria uma msg" com o texto "Vetor"
msg_comma:          .string ","                                 # "Cria uma msg" com o caractere ","
##  > $s0 = endereco_vetor
##  > $s1 = tamanho_vetor
.text
jal     main

main:
    li  s1, 8                                                   # n = 8 (size of array)
    
    ## > Imprime_vetor
    la      a0, vetor                                           # a0 = &vetor
    li      a1, 8                                               # a0 = N (tamanho vetor)

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     imprime_vetor                                       # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  

    ## > Atividade 1
    la      a0, vetor                                           # Carrega o endereço do vetor em a0
    li      a1, 8                                               # Carrega o tamanho do vetor em a1
    
    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     menor_vetor                                         # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  
    
    ## > Imprime_vetor
    la      a0, vetor                                           # a0 = &vetor
    li      a1, 8                                               # a0 = N (tamanho vetor)

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     imprime_vetor                                       # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  
    
    ## > Atividade 2
    la      a0, vetor                                           # Endereço do vetor
    li      a1, 0                                               # Indice i
    li      a2, 1                                               # Indice j

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     swap_vetor                                          # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  

    ## > Imprime_vetor
    la      a0, vetor                                           # a0 = &vetor
    li      a1, 8                                               # a0 = N (tamanho vetor)

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     imprime_vetor                                       # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  
    
    ## > Atividade 3
    la      a0, vetor                                           # Endereço do vetor
    li      a1, 8                                               # Tamanho

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     ord_menor_swap                                      # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  

    ## > Imprime_vetor
    la      a0, vetor                                           # a0 = &vetor
    li      a1, 8                                               # a0 = N (tamanho vetor)

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     imprime_vetor                                       # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer  

    nop
	ebreak

## > Atividade 1
# a0, a1
# menor_vetor(int *vetor, int tamanho_vetor)
# Retorna em a0 e a1 respectivamente o indice do menor valor e o valor
menor_vetor:
    li      t0, 0                                               # Variável de controle do loop
    li      t1, 0                                               # Deslocamento na memória
    lw      t2, 0(a0)                                           # Carrega o primeiro valor do vetor em t2  (menor valor)
    li      t3, 0                                               # Define o indíce do primeiro valor para t3 (índice do menor valor)

    addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
    sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
    jal     loop_menor_vetor                                    # Chama loop_display_vetor_values e linka ra a este ponto do código
    lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
    addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer

    ret                                                         # Retorna para onde foi chamada

    loop_menor_vetor: slt   t4, t0, a1                          # t4 = t0 < a1 ? 1 : 0
        beq     t4, zero, fim_loop_menor_vetor                  # Encerra o loop
        lw      t5, 0(a0)                                       # Carrega o valor de a0 em t5
        slt     t6, t5, t2                                      # t6 = t5 < t2 ? 1 : 0
        bne     t6, zero, novo_menor_valor                      # Vai para novo_menor valor
        
        addi    t0, t0, 1                                       # Incrementa em 1 o i
        slli    t1, t0, 2                                       # Atualiza o deslocamento na memória
        j       loop_menor_vetor                                # Retorna para o loop

        novo_menor_valor:
            lw      t2, 0(a0)                                   # Menor valor atualizado
            addi    t3, t0, 0                                   # �?ndice do menor valor atualizado
            addi    t0, t0, 1                                   # Incrementa em 1 o i
            slli    t1, t0, 2                                   # Atualiza o deslocamento na memória
            j       loop_menor_vetor                            # Retorna para o loop
        
        fim_loop_menor_vetor:
            add     a0, t3, zero                                # a0 = Menor valor
            add     a1, t2, zero                                # a1 = Indice menor valor
            ret


## > Atividade 2
# a0, a1, a2
# swap_vetor(int *vetor, int i, int j) // Indice i, indice j
# 
swap_vetor:
    slli    a1, a1 ,2                                           # Multiplica por 4 pra acessar a posição na word
    slli    a2, a2, 2                                           # Multiplica por 4 pra acessar a posição na word
    add     t0, a0, a1                                          # t0 = endereço da posição de i no vetor
    add     t1, a0, a2                                          # t1 = endereço da posição de j no vetor
    lw      t2, 0(t0)                                           # t2 = valor da posição i
    lw      t3, 0(t1)                                           # t2 = valor da posição j
    sw      t2, 0(t1)                                           # js = valor de i
    sw      t3, 0(t0)                                           # i = valor de j
    ret                                                         # Retorna pra ra
    
## > Atividade 3
# ord_menor_swap(int *vetor, int n) // n = tamanho vetor
# Ordena o vetor de forma crescente utilizando swap_vetor e menor_vetor
ord_menor_swap:
    li      s2, 0                                                   # Controle de loop
    li      s3, 0                                                   # Deslocamento na memória
    la      s0, vetor                                               # s0 = &vetor
    add     s1, a1, zero                                            # s1 = N
    # s1 == n
    loop_ord_menor_swap:    slt      s4, s2, s1                     # s4 = s2 < s1 ? 1 : 0
        bne      s4, zero, fim_loop_ord_menor_swap                  # se s4 == 0
        add      a0, s0, s3                                         # a0 = endereço de vetor + deslocamento no vetor
        add      a1, s1, zero                                       # a1 = N
        
        addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
        sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
        jal     menor_vetor                                         # Chama loop_display_vetor_values e linka ra a este ponto do código
        lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
        addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer

        add     a0, s0, s3                                          # a0 = endereço de vetor + deslocamento no vetor
        #a1 = indice do menor valor
        add     a2, s2, zero                                        # �?ndice atual do vetor

        addi    sp, sp, 4                                           # Incrementa uma posição do stack pointer
        sw      ra, 0(sp)                                           # Salva o valor do endereço de retorno no topo do stack pointer
        jal     swap_vetor                                          # Chama loop_display_vetor_values e linka ra a este ponto do código
        lw      ra, 0(sp)                                           # ra recebe o endereço salvo no topo do stack pointer
        addi    sp, sp, -4                                          # Decerementa uma posição do stack pointer

        slli    s3, s2, 2                                           # s3 recebe i * 4    
        addi    s2, s2, 1                                           # Incrementa i
    fim_loop_ord_menor_swap:
        ret

#finish_program:
#########################################################
# imprime_vetor
# argumentos: a0 - endereço inicial do vetor
#             a1 - tamanho do vetor
# retorno: ---- (nenhum retorno)
# registradores ocupados: a0 - argumento de entrada 
#			       e argumento para o ecall
#			  a1 - argumento de entrada
#			  a2 - ponteiro para o vetor
# 			  a7 - argumento para o ecall
# comentário: a função NÂO preserva os valores dos 
#	      argumentos passados para a função
#########################################################
	
imprime_vetor:
	add	a2, zero, a0	# transfere valor de a0 para a2

	la	a0, msg_vetor	# coloca endereço inicial da mensagem em a0
	li	a7, 4		    # carrega a7 com valor correspondente a impressao de string na chamada de sistema
	ecall			    # chamada de sistema (exception call)

laco_imp:	
	beq	a1, zero, fim	        # verifica se percorreu todo o vetor. Caso sim, desvia para fim
	lw	a0, 0(a2)	            # lê endereço atual do vetor e coloca em a0
	li	a7, 1		            # carrega a7 com valor correspondente a impressao de inteiro na chamada de sistema
	ecall			            # chamada de sistema (exception call)

	la	a0, msg_blank_space	    # coloca endereço inicial da mensagem em a0
	li	a7, 4		            # carrega a7 com valor correspondente a impressao de string na chamada de sistema
	ecall			            # chamada de sistema (exception call)
	
	addi	a2, a2, 4	        # faz a2 apontar para próxima posição do vetor
	addi 	a1, a1, -1 	        # decrementa variável de controle (para saber se percorreu todo o vetor)
	j	laco_imp	            # desvia para laco
	
fim:
	la	a0, msg_new_line # coloca endereço inicial da mensagem em a0	
	li	a7, 4		 # carrega a7 com valor correspondente a impressao de string na chamada de sistema
	ecall			 # chamada de sistema (exception call)
	ret	
		
######################################################	