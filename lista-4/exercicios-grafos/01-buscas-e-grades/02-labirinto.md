# 02 - Labirinto

## Tema

BFS, menor caminho sem pesos e reconstrução do caminho.

## Problema

Uma grade contém paredes (`#`), espaços livres (`.`), um início (`A`) e um destino (`B`). Encontre o menor caminho de `A` até `B`, movendo-se nas quatro direções.

## Entrada

- `n m`: dimensões da grade.
- `n` linhas descrevendo o labirinto.

## Saída

- `NO`, caso não exista caminho.
- Caso exista, imprima `YES`, o tamanho e uma sequência formada por `U`, `D`, `L` e `R`.

## Exemplo

```text
Entrada
5 8
########
#.A#...#
#.##.#B#
#......#
########

Saída possível
YES
9
LDDRRRRRU
```

## Dicas graduais

1. BFS encontra o menor caminho quando cada movimento custa 1.
2. Ao visitar uma célula, guarde de qual direção você chegou.
3. Reconstrua o caminho começando em `B` e voltando até `A`.

## Meta

Entender por que marcar uma célula ao inseri-la na fila evita repetições.

