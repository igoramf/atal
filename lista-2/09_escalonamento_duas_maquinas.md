# 9. Escalonamento em Duas Maquinas

Voce tem `n` tarefas. A tarefa `i` demora `t[i]` unidades de tempo. Cada tarefa deve ser executada em exatamente uma de duas maquinas.

As maquinas trabalham em paralelo. O tempo final e o maior tempo total entre as duas maquinas. Minimize esse tempo final.

## Entrada

```text
n
t1 t2 ... tn
```

## Saida

```text
menor tempo final
```

## Exemplo

```text
Entrada:
5
2 4 7 8 9

Saida:
15
```

## Classificacao

Branch and Bound.
