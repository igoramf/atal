# 05 - Party

[Problema original no Codeforces](https://codeforces.com/problemset/problem/115/A)

## Problema

Uma empresa possui `n` funcionários. Cada funcionário tem um gerente imediato ou não possui gerente. Divida os funcionários no menor número possível de grupos, de forma que nenhum grupo contenha simultaneamente um funcionário e algum superior dele, direto ou indireto.

É garantido que a hierarquia não possui ciclos.

## Entrada

- A primeira linha contém `n`.
- As próximas `n` linhas contêm `p[i]`, o gerente do funcionário `i`.
- `p[i] = -1` significa que o funcionário não possui gerente.

## Saída

Imprima a quantidade mínima de grupos.

## Restrições

```text
1 <= n <= 2000
p[i] = -1 ou 1 <= p[i] <= n
p[i] != i
```

## Exemplo

```text
Entrada
5
-1
1
2
1
-1

Saída
3
```
