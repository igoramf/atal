# F. Olimpiadas

## Enunciado

Voce tem `n` problemas. Voce avaliou a dificuldade do i-esimo problema como o
numero inteiro `ci`. Agora, quer montar um conjunto de problemas para um
concurso, usando alguns dos problemas que criou.

O conjunto para o concurso deve ter pelo menos dois problemas.

Voce acha que a soma das dificuldades dos problemas escolhidos deve ser pelo
menos `l` e no maximo `r`.

Alem disso, a diferenca entre a dificuldade do problema mais facil e do mais
dificil do conjunto deve ser pelo menos `x`.

Descubra de quantas formas e possivel escolher um conjunto de problemas que
atenda a esses criterios.

## Entrada

A primeira linha contem quatro inteiros:

```text
n l r x
```

com:

```text
1 <= n <= 15
1 <= l <= r <= 10^9
1 <= x <= 10^6
```

Eles representam, respectivamente:

- `n`: o numero de problemas disponiveis;
- `l`: a soma minima das dificuldades do conjunto;
- `r`: a soma maxima das dificuldades do conjunto;
- `x`: a diferenca minima entre o problema mais dificil e o mais facil.

A segunda linha contem `n` inteiros:

```text
c1 c2 ... cn
```

com:

```text
1 <= ci <= 10^6
```

Esses valores representam as dificuldades dos problemas.

## Saida

Imprima o numero de maneiras de escolher um conjunto de problemas adequado para
o concurso.

## Exemplos

Exemplo 1:

Entrada:

```text
3 5 6 1
1 2 3
```

Saida:

```text
2
```

Exemplo 2:

Entrada:

```text
4 40 50 10
10 20 30 25
```

Saida:

```text
2
```

Exemplo 3:

Entrada:

```text
5 25 35 10
10 10 20 10 20
```

Saida:

```text
6
```

## Nota

No primeiro exemplo, dois conjuntos sao validos: um com o segundo e o terceiro
problema, e outro com os tres problemas.

No segundo exemplo, dois conjuntos sao validos: o conjunto com dificuldades `10`
e `30`, e o conjunto com dificuldades `20` e `30`.

No terceiro exemplo, qualquer conjunto com um problema de dificuldade `10` e
outro de dificuldade `20` serve.

