# 04 - Dijkstra?

[Problema original no Codeforces](https://codeforces.com/problemset/problem/20/C)

## Problema

Você recebe um grafo não direcionado e ponderado com vértices de `1` até `n`. Encontre um caminho de menor custo do vértice `1` até o vértice `n`.

## Entrada

- A primeira linha contém `n m`.
- As próximas `m` linhas contêm `a b w`: uma aresta entre `a` e `b` com peso `w`.
- Podem existir laços e arestas repetidas.

## Saída

Imprima os vértices do menor caminho, na ordem em que são visitados. Se não existir caminho, imprima `-1`. Qualquer menor caminho é aceito.

## Restrições

```text
2 <= n <= 100000
0 <= m <= 100000
1 <= w <= 1000000
```

## Exemplo

```text
Entrada
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1

Saída possível
1 4 3 5
```
