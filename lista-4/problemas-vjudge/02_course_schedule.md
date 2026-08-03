# 02 - Course Schedule

[Problema original no CSES](https://cses.fi/problemset/task/1679/)

## Problema

Você precisa concluir `n` cursos. Cada requisito `a b` significa que o curso `a` precisa ser concluído antes do curso `b`. Encontre uma ordem que respeite todos os requisitos.

## Entrada

- A primeira linha contém `n m`: cursos e requisitos.
- Cada uma das próximas `m` linhas contém um requisito `a b`.

## Saída

Imprima uma ordem válida contendo todos os cursos. Se isso for impossível, imprima `IMPOSSIBLE`.

## Restrições

```text
1 <= n <= 100000
1 <= m <= 200000
1 <= a,b <= n
```

## Exemplo

```text
Entrada
5 3
1 2
3 1
4 5

Saída possível
3 4 1 5 2
```
