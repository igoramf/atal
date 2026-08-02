# 13 - Conectar regiões

## Tema

Componentes conexos em grade e comparação entre componentes.

## Problema

Uma grade quadrada contém células livres e bloqueadas. Duas posições são fornecidas. É possível atravessar gratuitamente dentro de cada região conectada. Se as posições estiverem em regiões diferentes, calcule o menor custo quadrático para conectá-las diretamente.

O custo entre `(x1, y1)` e `(x2, y2)` é:

```text
(x1 - x2)^2 + (y1 - y2)^2
```

## Entrada

- `n`.
- As duas posições.
- `n` linhas contendo `0` para livre e `1` para bloqueada.

## Saída

Imprima o menor custo de conexão.

## Dicas graduais

1. Descubra o componente da primeira posição.
2. Descubra o componente da segunda posição.
3. Compare todos os pares de células dos dois componentes.

## Meta

Reutilizar BFS ou DFS para obter explicitamente os vértices de um componente.

