# 10. Clique Maxima

Dado um grafo nao direcionado com `n` vertices e `m` arestas, encontre o tamanho da maior clique.

Uma clique e um conjunto de vertices em que todo par de vertices distintos possui uma aresta entre si.

## Entrada

```text
n m
u1 v1
u2 v2
...
um vm
```

Os vertices sao numerados de `0` ate `n - 1`.

## Saida

```text
tamanho da maior clique
```

## Exemplo

```text
Entrada:
5 6
0 1
0 2
1 2
1 3
2 3
3 4

Saida:
3
```

## Classificacao

Branch and Bound.
