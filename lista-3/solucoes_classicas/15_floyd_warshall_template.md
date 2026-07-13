# Floyd-Warshall

## Enunciado

Dado um grafo direcionado com `n` vertices e `m` arestas ponderadas, calcule a
menor distancia entre todos os pares de vertices.

Os vertices da entrada sao numerados de `1` a `n`.

## Entrada

```text
n m
a1 b1 w1
a2 b2 w2
...
am bm wm
```

## Saida

Imprima uma matriz `n x n` com as menores distancias. Se nao existir caminho,
imprima `-1`.

## Exemplo

Entrada:

```text
3 3
1 2 5
2 3 7
1 3 20
```

Saida:

```text
0 5 12
-1 0 7
-1 -1 0
```
