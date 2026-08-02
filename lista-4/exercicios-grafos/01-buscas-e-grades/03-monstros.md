# 03 - Monstros

## Tema

BFS com múltiplas fontes e comparação de tempos de chegada.

## Problema

Um jogador (`A`) está em um labirinto com monstros (`M`). A cada segundo, jogador e monstros podem avançar uma célula nas quatro direções. Descubra se o jogador consegue alcançar alguma borda sem ocupar uma célula no mesmo instante ou depois de um monstro.

## Entrada

- `n m`: dimensões da grade.
- A grade com paredes (`#`), espaços livres (`.`), um jogador e zero ou mais monstros.

## Saída

- `NO`, se não houver fuga segura.
- Caso contrário, `YES`, o tamanho do caminho e os movimentos.

## Dicas graduais

1. Comece uma BFS colocando todos os monstros na fila ao mesmo tempo.
2. Calcule o primeiro instante em que um monstro alcança cada célula.
3. Na BFS do jogador, só avance se ele chegar estritamente antes do monstro.

## Meta

Perceber que “vários monstros” não exigem uma BFS separada para cada um.

