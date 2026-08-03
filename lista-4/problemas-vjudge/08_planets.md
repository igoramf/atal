# 08 - Planets

[Problema original no Codeforces](https://codeforces.com/problemset/problem/229/B)

## Problema

Existem `n` planetas ligados por portais de mão dupla. Jack começa no planeta `1`, no instante `0`, e quer chegar ao planeta `n` o mais cedo possível.

Em cada planeta existem instantes bloqueados. Se Jack estiver naquele planeta em um instante bloqueado, precisa esperar até o primeiro instante seguinte que não esteja bloqueado antes de usar um portal. Chegar ao planeta de destino encerra a viagem imediatamente.

## Entrada

- A primeira linha contém `n m`.
- As próximas `m` linhas contêm `a b c`: planetas ligados e tempo de viagem.
- Depois existem `n` linhas, uma por planeta. Cada linha começa com `k`, seguido pelos `k` instantes bloqueados em ordem crescente.

## Saída

Imprima o menor instante possível de chegada ao planeta `n`. Se ele for inalcançável, imprima `-1`.

## Restrições

```text
2 <= n <= 100000
0 <= m <= 100000
1 <= c <= 10000
0 <= instante bloqueado < 1000000000
soma de todos os k <= 100000
```

## Exemplo

```text
Entrada
4 6
1 2 2
1 3 3
1 4 8
2 3 4
2 4 5
3 4 3
0
1 3
2 3 4
0

Saída
7
```
