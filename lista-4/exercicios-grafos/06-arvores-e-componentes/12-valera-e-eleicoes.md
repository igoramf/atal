# 12 - Valera e eleições

## Tema

DFS em árvore e informação propagada dos filhos para o pai.

## Problema

Uma cidade é representada por uma árvore enraizada no vértice 1. Cada estrada é normal ou problemática. Escolha o menor conjunto de vértices capaz de cobrir os caminhos que contêm estradas problemáticas, seguindo a condição descrita no exercício original.

## Entrada

- `n` vértices.
- `n - 1` linhas `x y t`, em que `t = 2` indica uma estrada problemática.

## Saída

Imprima a quantidade de vértices escolhidos e seus identificadores.

## Dicas graduais

1. Enraíze a árvore no vértice 1.
2. Processe os filhos antes de decidir sobre o vértice atual.
3. Uma aresta problemática pode ser coberta pelo primeiro vértice adequado abaixo dela.

## Meta

Praticar DFS pós-ordem: a resposta do filho influencia a decisão do pai.

