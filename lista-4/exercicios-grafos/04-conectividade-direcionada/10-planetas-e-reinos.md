# 10 - Planetas e reinos

## Tema

Componentes fortemente conexos e algoritmo de Kosaraju.

## Problema

Agrupe os vértices de um grafo dirigido em reinos. Dois vértices pertencem ao mesmo reino quando cada um consegue alcançar o outro.

## Entrada

- `n m`.
- `m` arestas dirigidas.

## Saída

- A quantidade de componentes fortemente conexos.
- O identificador do componente de cada vértice.

## Dicas graduais

1. Na primeira DFS, guarde os vértices na ordem de término.
2. Inverta todas as arestas.
3. Visite os vértices na ordem de término invertida, criando um componente por busca.

## Meta

Entender a diferença entre componente conexo e componente fortemente conexo.

