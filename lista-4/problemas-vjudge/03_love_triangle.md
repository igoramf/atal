# 03 - Love Triangle

[Problema original no Codeforces](https://codeforces.com/problemset/problem/939/A)

## Problema

Existem `n` aviões. Cada avião `i` gosta exatamente do avião `f[i]`. Verifique se existem três aviões distintos `A`, `B` e `C` tais que `A` gosta de `B`, `B` gosta de `C` e `C` gosta de `A`.

## Entrada

- A primeira linha contém `n`.
- A segunda linha contém `f[1], f[2], ..., f[n]`.

## Saída

Imprima `YES` se existir um ciclo de tamanho 3; caso contrário, imprima `NO`.

## Restrições

```text
2 <= n <= 5000
1 <= f[i] <= n
f[i] != i
```

## Exemplos

```text
Entrada
5
2 4 5 1 3

Saída
YES
```

```text
Entrada
5
5 5 5 5 1

Saída
NO
```
