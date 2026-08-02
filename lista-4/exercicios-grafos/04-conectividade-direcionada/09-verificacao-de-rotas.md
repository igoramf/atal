# 09 - Verificação de rotas

## Tema

Alcançabilidade em grafo dirigido e grafo reverso.

## Problema

Determine se, para qualquer par de cidades `a` e `b`, existe uma rota de `a` até `b`. Caso não exista, mostre um par que serve de contraexemplo.

## Entrada

- `n m`.
- `m` arestas dirigidas `a b`.

## Saída

- `YES`, se todas as cidades alcançam todas as outras.
- Caso contrário, `NO` e um par `a b` para o qual não há caminho de `a` até `b`.

## Dicas graduais

1. Faça DFS a partir do vértice 1 no grafo original.
2. Faça outra DFS a partir de 1 com todas as arestas invertidas.
3. Pense no significado de falhar em cada uma dessas buscas.

## Meta

Resolver com apenas duas buscas, em `O(n + m)`.

