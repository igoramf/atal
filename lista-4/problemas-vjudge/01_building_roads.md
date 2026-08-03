# 01 - Building Roads

[Problema original no CSES](https://cses.fi/problemset/task/1666/)

## Problema

Existem `n` cidades e `m` estradas de mão dupla. Construa a menor quantidade possível de novas estradas para que exista uma rota entre qualquer par de cidades. Informe também quais estradas devem ser construídas.

## Entrada

- A primeira linha contém `n m`.
- As próximas `m` linhas contêm `a b`, indicando uma estrada entre as cidades `a` e `b`.

## Saída

- Imprima `k`, a quantidade mínima de novas estradas.
- Depois, imprima `k` pares de cidades que devem ser conectadas.
- Qualquer solução mínima válida é aceita.

## Restrições

```text
1 <= n <= 100000
1 <= m <= 200000
1 <= a,b <= n
```

## Exemplo

```text
Entrada
4 2
1 2
3 4

Saída possível
1
2 3
```
