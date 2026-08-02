# 07 - Desconto em voo

## Tema

Dijkstra no grafo original e no grafo reverso.

## Problema

Encontre o menor custo da cidade 1 até a cidade `n`. É permitido aplicar uma vez um cupom que reduz pela metade, com divisão inteira, o custo de exatamente um voo.

## Entrada

- `n m`.
- `m` voos dirigidos `a b c`.

## Saída

Imprima o menor custo possível.

## Dicas graduais

1. Calcule as distâncias de 1 até todos os vértices.
2. Inverta as arestas e calcule as distâncias de `n` até todos os vértices.
3. Teste cada aresta `a -> b` como a aresta que recebe o desconto.

## Fórmula útil

```text
distancia_de_1[a] + custo(a,b)//2 + distancia_ate_n[b]
```

## Meta

Entender por que o grafo reverso fornece a distância de qualquer vértice até `n`.

