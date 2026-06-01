# 12. Comercio de Vinho em Gergovia

## Enunciado

Em uma rua existem `n` casas. Cada casa possui um inteiro:

- valor positivo: a casa quer vender essa quantidade de vinho;
- valor negativo: a casa quer comprar essa quantidade de vinho.

A soma de todos os valores sempre e `0`.

Mover uma unidade de vinho por uma casa de distancia custa `1` unidade de
trabalho. Calcule o menor trabalho necessario para satisfazer todos os
compradores e vendedores.

## Entrada

A entrada contem varios casos de teste.

Cada caso comeca com um inteiro `n`. Se `n = 0`, a entrada termina.

Na linha seguinte, existem `n` inteiros:

```text
a1 a2 ... an
```

## Saida

Para cada caso de teste, imprima o menor trabalho necessario.

## Restricoes

```text
1 <= n <= 100000
-1000 <= ai <= 1000
sum(ai) = 0
```

## Exemplo

Entrada:

```text
5
5 -4 1 -3 1
0
```

Saida:

```text
9
```
