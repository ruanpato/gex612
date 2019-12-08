# Programação assembly Risc-V [:link:](https://github.com/ruanpato/gex612/tree/master/programacao_assembly_risc-v) #

Este trabalho é um dos trabalhos menores que compõem as Notas Parciais (NP) da matéria Organização de Computadores cursada no segundo semestre de 2019 referente a graduação em Ciência da computação.

## Sumário ##

- [Programação assembly Risc-V :link:](#programa%c3%a7%c3%a3o-assembly-risc-v-link)
  - [Sumário](#sum%c3%a1rio)
  - [1. Grupo](#1-grupo)
  - [2. Descrição](#2-descri%c3%a7%c3%a3o)
  - [6. Ferramentas utilizadas](#6-ferramentas-utilizadas)
  - [7. Professor](#7-professor)

## 1. Grupo ##

- **[Ruan Pato](https://github.com/ruanpato)** - Descrição em README.md e desenvolvimento do trabalho.

## 2. Descrição ##

[1.](https://github.com/ruanpato/gex612/tree/master/programacao_assembly_risc-v/menor.asm) Implemente uma função chamada "Menor" que recebe 3 números inteiros  (nos registradores  a0, a1 e a2) e retorna o menor deles no registrador s0.

Observe o código da chamada da função :

```assembly
main:

   addi a0, zero, "valor de teste 1"

   addi a1, zero, "valor de teste 2"

   addi a2, zero, "valor de teste 3"

   jal Menor

   nop

   break

Menor:

      # sua função aqui

      return
```

[2.](https://github.com/ruanpato/gex612/tree/master/programacao_assembly_risc-v/triangulo.asm) Elaborar uma função chamada "Triangulo" que recebe 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores são inteiros e positivos. (se X > y + z não formam triângulo, supondo que x é o maior).

[3.](https://github.com/ruanpato/gex612/tree/master/programacao_assembly_risc-v/multiplica.asm) Fazer uma função chamada "Multiplica" que recebe dois números inteiros positivos e retorna o valor da multiplicação entre eles. [exercicio_1.asm](https://github.com/ruanpato/gex612/tree/master/programacao_assembly_risc-v/exercicio_1.asm)

## 6. Ferramentas utilizadas ##

- [RARS](https://github.com/TheThirdOne/rars) - RISC-V Assembler and Runtime Simulator

## 7. Professor ##

- [Me. Luciano Lores Caimi](https://github.com/lcaimi) - *descrição do trabalho em [pdf](https://github.com/ruanpato/gex612/tree/master/simulador_cache/Trabalho_Mapeamento_MP-Cache.pdf).*
