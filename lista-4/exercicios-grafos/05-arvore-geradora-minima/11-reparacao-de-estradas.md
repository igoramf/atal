# 11 - Reparação de estradas

## Tema

Árvore geradora mínima, Kruskal e Union-Find.

## Problema

Escolha um conjunto de estradas para conectar todas as cidades pelo menor custo total. Se não for possível conectar todas, informe isso.

## Entrada

- `n m`.
- `m` estradas não direcionadas `a b c`.

## Saída

Imprima o menor custo ou `IMPOSSIBLE`.

## Dicas graduais

1. Ordene as arestas pelo custo.
2. Aceite uma aresta somente quando ela conecta componentes diferentes.
3. Use Union-Find para testar e unir componentes.
4. Uma árvore com `n` vértices precisa usar exatamente `n - 1` arestas.

## Meta

Implementar `find` com compressão de caminho e `union` por tamanho ou rank.

