# 7. Alocacao de Tarefas

Existem `n` trabalhadores e `n` tarefas. O custo de atribuir a tarefa `j` ao trabalhador `i` e `c[i][j]`.

Cada trabalhador deve receber exatamente uma tarefa, e cada tarefa deve ser usada exatamente uma vez. Minimize o custo total.

## Entrada

```text
n
c11 c12 ... c1n
c21 c22 ... c2n
...
cn1 cn2 ... cnn
```

## Saida

```text
menor custo total
```

## Exemplo

```text
Entrada:
4
9 2 7 8
6 4 3 7
5 8 1 8
7 6 9 4

Saida:
13
```

## Classificacao

Branch and Bound.
