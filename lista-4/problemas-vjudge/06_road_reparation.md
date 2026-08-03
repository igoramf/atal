# 06 - Road Reparation

[Problema original no CSES](https://cses.fi/problemset/task/1675/)

## Problema

Existem `n` cidades e `m` estradas de mão dupla, todas inicialmente inutilizáveis. Cada estrada possui um custo de reparação. Escolha quais estradas reparar para conectar todas as cidades com o menor custo total.

## Entrada

- A primeira linha contém `n m`.
- As próximas `m` linhas contêm `a b c`: extremidades e custo de reparação.

## Saída

Imprima o menor custo total. Caso seja impossível conectar todas as cidades, imprima `IMPOSSIBLE`.

## Restrições

```text
1 <= n <= 100000
1 <= m <= 200000
1 <= c <= 1000000000
```

## Exemplo

```text
Entrada
5 6
1 2 3
2 3 5
2 4 2
3 4 8
5 1 7
5 4 4

Saída
14
```
