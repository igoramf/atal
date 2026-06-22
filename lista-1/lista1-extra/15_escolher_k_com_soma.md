# 15. Escolher K Numeros com Soma Alvo

## Enunciado

Dado um array com `n` inteiros positivos, um inteiro `k` e um alvo `S`, conte
quantas formas existem de escolher exatamente `k` elementos cuja soma seja
igual a `S`.

Cada elemento pode ser escolhido no maximo uma vez.

## Entrada

A primeira linha contem tres inteiros:

```text
n k S
```

A segunda linha contem `n` inteiros:

```text
v1 v2 ... vn
```

## Saida

Imprima um unico inteiro: a quantidade de formas de escolher exatamente `k`
elementos com soma `S`.

## Restricoes

```text
1 <= n <= 20
1 <= k <= n
1 <= vi <= 100
1 <= S <= 1000
```

## Exemplo

Entrada:

```text
5 2 6
1 2 3 4 5
```

Saida:

```text
2
```

Explicacao:

```text
1 + 5 = 6
2 + 4 = 6
```
