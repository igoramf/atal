# 01 - Contando salas

## Tema

BFS ou DFS, componentes conexos e representação implícita de uma grade como grafo.

## Problema

Você recebe a planta de um prédio. Cada posição é piso (`.`) ou parede (`#`). É possível andar para cima, baixo, esquerda ou direita. Conte quantas salas existem; uma sala é um conjunto máximo de pisos conectados.

## Entrada

- `n m`: altura e largura da planta.
- `n` linhas com `m` caracteres.

## Saída

Imprima a quantidade de salas.

## Exemplo

```text
Entrada
5 8
########
#..#...#
####.#.#
#..#...#
########

Saída
3
```

## Dicas graduais

1. Percorra todas as células.
2. Ao encontrar um piso ainda não visitado, uma nova sala foi descoberta.
3. Execute BFS ou DFS para marcar toda essa sala.

## Meta

Resolver em `O(n * m)` sem consultar a solução.

