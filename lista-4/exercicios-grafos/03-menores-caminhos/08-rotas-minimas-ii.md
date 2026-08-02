# 08 - Rotas mínimas II

## Tema

Floyd-Warshall e menores caminhos entre todos os pares.

## Problema

Um grafo não direcionado possui estradas com custos. Responda várias consultas perguntando o menor custo entre dois vértices.

## Entrada

- `n m q`: cidades, estradas e consultas.
- `m` linhas `a b c`.
- `q` linhas `a b`.

## Saída

Para cada consulta, imprima a menor distância ou `-1` se não existir caminho.

## Dicas graduais

1. Crie uma matriz de distâncias e coloque zero na diagonal.
2. Se houver arestas repetidas, preserve o menor custo.
3. Para cada intermediário `k`, tente melhorar `dist[i][j]` passando por `k`.

## Meta

Saber explicar a transição `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.

