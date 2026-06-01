# 10. Labirinto com Menor Caminho

## Enunciado

Dada uma matriz com inicio `S`, fim `E`, celulas livres `.` e bloqueadas `#`,
encontre o tamanho do menor caminho de `S` ate `E`.

Voce pode se mover para cima, baixo, esquerda e direita.

Se nao existir caminho, imprima `-1`.

## Entrada

A primeira linha contem dois inteiros:

```text
n m
```

As proximas `n` linhas contem a matriz.

## Saida

Imprima um unico inteiro: o tamanho do menor caminho, ou `-1` se nao houver
caminho.

## Exemplo

Entrada:

```text
3 3
S..
##.
..E
```

Saida:

```text
4
```

