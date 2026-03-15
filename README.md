# Disponibilidade de Serviço Replicado

## Descrição
Este trabalho da disciplina de **Computação Distribuída** tem como objetivo calcular a **disponibilidade de um serviço replicado em múltiplos servidores**, considerando:

- **n**: número total de servidores  
- **k**: número mínimo de servidores disponíveis para o serviço funcionar  
- **p**: probabilidade de cada servidor estar disponível  

---

## Fórmula

A disponibilidade do serviço é dada por:

\[
A(n,k,p)=\sum_{i=k}^{n}\binom{n}{i}p^i(1-p)^{n-i}
\]

Essa fórmula representa a probabilidade de existirem **pelo menos \(k\) servidores disponíveis** entre os \(n\) servidores.

---

## Casos Extremos

- **Se \(k=1\)**:  
\[
A(n,1,p)=1-(1-p)^n
\]

- **Se \(k=n\)**:  
\[
A(n,n,p)=p^n
\]

---

## Resposta Comentada
A fórmula foi deduzida a partir da probabilidade de existirem **exatamente \(i\) servidores disponíveis** entre \(n\).  

- \(\binom{n}{i}\): quantidade de combinações possíveis  
- \(p^i\): probabilidade de \(i\) servidores estarem disponíveis  
- \((1-p)^{n-i}\): probabilidade dos demais estarem indisponíveis  

Como o serviço funciona com **pelo menos \(k\)** servidores disponíveis, somamos os casos de \(i=k\) até \(i=n\).

---

---

## Classe em Python
O projeto possui uma classe chamada `DisponibilidadeServico`, responsável por:

- receber os valores de **n**, **k** e **p**
- validar os parâmetros informados
- calcular a disponibilidade do serviço com base na fórmula matemática

A classe utiliza a função `comb()` da biblioteca `math`, que calcula a combinação \(\binom{n}{i}\), ou seja, a quantidade de formas de escolher `i` servidores disponíveis entre `n`.

O programa também permite que o usuário informe os valores pelo terminal, tornando a execução mais simples e interativa.

---

## Integrantes
- Victor Sucupira - 1410777
- Lucas Fontenele - 1810490
- diego antonioli - 2214654

---

## Repositório sugerido
`distributed-service-availability`