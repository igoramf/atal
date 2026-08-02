# 04 - Bloqueando o labirinto

## Tema

DFS iterativa e manutenção de uma região conectada.

## Problema

Uma grade possui células livres (`.`) e paredes (`#`). Transforme exatamente `k` células livres em `X`, mantendo todas as células livres restantes conectadas.

## Entrada

- `n m k`.
- `n` linhas com a grade.

## Saída

Imprima a grade resultante.

## Dicas graduais

1. Conte quantas células deverão continuar livres.
2. Inicie uma DFS em qualquer célula livre.
3. Preserve apenas as primeiras células visitadas e transforme o restante em `X`.

## Meta

Fazer a busca com uma pilha para evitar limite de recursão em grades grandes.

