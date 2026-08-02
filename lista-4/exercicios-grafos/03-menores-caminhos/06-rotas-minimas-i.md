# 06 - Rotas mínimas I

## Tema

Dijkstra em grafo direcionado com pesos positivos.

## Problema

Há `n` cidades e `m` voos direcionados. Cada voo tem um custo positivo. Calcule o menor custo da cidade 1 para todas as cidades.

## Entrada

- `n m`.
- `m` linhas com `a b c`: voo de `a` para `b` com custo `c`.

## Saída

Imprima `n` distâncias, da cidade 1 até cada cidade.

## Dicas graduais

1. Guarde pares `(vizinho, peso)` na lista de adjacência.
2. Use uma fila de prioridade com `(distância, vértice)`.
3. Ignore entradas antigas da fila cuja distância seja maior que a melhor conhecida.

## Meta

Resolver em `O((n + m) log n)`.

