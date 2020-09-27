# Programação assembly RISC-V: Acesso a memória #

[código](https://github.com/ruanpato/risc-v/tree/master/acesso_a_memoria/acesso_a_memoria.s).

1) Implemente uma função chamada "menor_vetor" que recebe o endereço inicial de um vetor e seu tamanho (nos registradores  a0 e a1 respectivamente) e retorna  o índice do menor valor e qual é este valor (nos registradores  a0 e a1 respectivamente).

2) Implemente uma função chamada "swap_vetor" que recebe o endereço inicial de um vetor e dois índices (nos registradores  a0, a1  e a2 respectivamente). A função deve realizar a troca dos valores presentes nos dois indices recebidos. Exemplo: Considerando o vetor armazendando os valores 2, 3, 1, -4, 6. Ao receber os indices 0 e 3 a função deve trocar de posição os valores 2 e -4. O valor final do vetor será: -4, 3, 1, 2, 6.

3) Utilizando as funções anteriores (menor_vetor e swap_vetor) implemente uma função que  recebe o endereço inicial de um vetor e seu tamanho (nos registradores  a0 e a1 respectivamente) e ordena este vetor de forma crescente.

## Ferramentas utilizadas ##
* [RARS](https://github.com/TheThirdOne/rars) - RISC-V Assembler and Runtime Simulator

### Autores ###

* **Ruan Pato** - *Exercícios e trabalhos feitos* - [Ruan Pato](https://github.com/ruanpato)
* **Me. Luciano Lores Caimi** - *Professor*