# Simulador Cache :computer: #

Este trabalho é um dos "grandes" trabalhos que compõem as Notas Parciais (NP) da matéria Organização de Computadores cursada no segundo semestre de 2019 referente a graduação em Ciência da computação.

## Sumário ##

- [Simulador Cache :computer:](#simulador-cache-computer)
  - [Sumário](#sum%c3%a1rio)
  - [1. Grupo](#1-grupo)
  - [2. Datas](#2-datas)
  - [3. Instruções de Entrega](#3-instru%c3%a7%c3%b5es-de-entrega)
  - [4. Instruções para implementação](#4-instru%c3%a7%c3%b5es-para-implementa%c3%a7%c3%a3o)
  - [5. Políticas](#5-pol%c3%adticas)
  - [6. Ferramentas utilizadas](#6-ferramentas-utilizadas)
  - [7. Professor](#7-professor)
  - [8. Como usar](#8-como-usar)
    - [Testes automatizados](#testes-automatizados)

## 1. Grupo ##

- **[Ruan Pato](https://github.com/ruanpato)** - Descrição em README.md e desenvolvimento do trabalho.  

## 2. Datas ##

**Data de entrega:** 09/12/2019 23:55 (UTC-3)  

## 3. Instruções de Entrega ##

Convidar o professor para o projeto.
Entregar via [moodle uffs](https://moodle-academico.uffs.edu.br) <sup>[*](#moodle-footnote)</sup>.

<a name="moodle-footnote">*</a>: [moodle](https://moodle.org/) é um software livre, de apoio à aprendizagem, executado num ambiente virtual.

## 4. Instruções para implementação ##

- Número de células na Memória Principal (MP): 128;
- Tamanho do bloco da MP: 4 células;
- Número de linhas da Memória Cache (MC): 8;
- Tamanho da célula de memória: 8 bits;
- Número de linhas do conjunto: 2 ou 4 linhas (definida pelo número entre parênteses ao lado da política de cada grupo);  

Cada dupla deve implementar a política de mapeamento, substituição e escrita conforme designado na folha a seguir.  
Na interface do programa deve ser apresentado todo o conteúdo da memória principal, da memória cache.  
Na MP deve-se mostrar o endereço de cada célula e o número do bloco da mesma. 
Na MC deve-se mostrar o conteúdo da linha, o número da linha, o bit de validade, o rótulo, os bits da política de substituição, o bit de escrita.  

**O programa deve apresentar um menu que dê acesso às seguintes operações:**  

- **Ler um endereço de memória:**
  - o usuário informa o endereço que deseja ler na MP.
  - Esta ação faz com que as políticas da cache sejam aplicadas.
  - Ao final do processo é informado ao usuário qual o valor presente no endereço e se houve um erro (miss) ou um acerto (hit) no acesso a cache.
  - Deve-se informar também qual o bloco na MP que se refere o endereço e qual a linha da cache o dado está armazenado (o conjunto também deve ser informado quando se aplica a situação);
- **Escrever na memória:**
  - o usuário informa o endereço e o dado a ser escrito na MP;
  - As políticas da cache devem ser aplicadas;
  - Ao final do processo é informado ao usuário se houve um erro (miss) ou um acerto (hit) no acesso a cache;
  - Deve-se informar também qual o bloco na MP que se refere o endereço e qual a linha da cache o dado está armazenado (o conjunto também deve ser informado quando se aplica a situação).
- **Apresentar as estatísticas:** esta opção apresenta para o usuário:
  - a quantidade de acessos realizadas;
  - a quantidade de leituras realizadas;
    - a quantidade de acertos de leitura;
    - a quantidade de erros de leitura;
  - a quantidade de escritas realizadas;
    - a quantidade de acertos de escrita;
    - a quantidade de erros de escrita.
  - Para acertos e faltas deve-se mostrar o valor absoluto e o valor percentual;
- **Encerrar o programa.**  

**OBS1:** Os valores e endereços devem ser apresentados em hexadecimal ou binário.  
**OBS2:** Os contadores da política de substituição possuem 4 bits (valor máximo 15).  
**OBS3.** Inicializar a MP com valores randômicos.  

## 5. Políticas ##

Mapeamento Associativo por Conjuntos (4)

- Escrita no retorno
- LRU

## 6. Ferramentas utilizadas ##

- [Python 3](https://www.python.org) - Python 3.6 intepreter.

## 7. Professor ##

- [Me. Luciano Lores Caimi](https://github.com/lcaimi) - *descrição do trabalho em [pdf](https://github.com/ruanpato/gex612/tree/master/simulador_cache/Trabalho_Mapeamento_MP-Cache.pdf).*

## 8. Como usar ##

Em ambiente linux via terminal estando no diretório do arquivo fonte para compilar, executar e testar manualmente basta rodar o seguinte comando:

```bash
python3 main.py
```

### Testes automatizados ###

Os testes automatizados visam objetivam trazer casos que mostrem parte do comportamento da cache de acordo com a [Políticas](#5-pol%c3%adticas) especificadas.

**Caso de Teste 0:**

Neste caso será feita a escrita do valor 11111111₁₀ (255₂) na primeira "célula da memória principal", após isso será feita a leitura de 4 diferentes blocos da memória principal que têm como destino o mesmo conjunto que o valor que foi escrito inicialmente. Testando assim o Write-Back no caso de leitura.

```bash
python3 main.py < in0
```

**Caso de Teste 1:**

Neste caso será feita a escrita do valor 11111110₁₀ (254₂) na primeira "célula da memória principal", após isso será feita a leitura de 3 diferentes blocos da memória principal e a escrita em uma célula pertecente à um bloco difente destes outros que têm como destino o mesmo conjunto que o valor que foi escrito inicialmente. Testando assim o Write-Back no caso de escrita em uma nova célula.

```bash
python3 main.py < in1
```
