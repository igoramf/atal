# B. Apenas Pluses

## Enunciado

Kmes escreveu três inteiros `a`, `b` e `c` para se lembrar de que precisa dar
`a * b * c` bananas para Noobish_Monk.

Noobish_Monk encontrou esses números e decidiu fazer a seguinte operação no
máximo 5 vezes:

- escolher um desses inteiros;
- aumentá-lo em `1`.

Por exemplo, se `a = 2`, `b = 3` e `c = 4`, é possível aumentar `a` três vezes
em `1` e aumentar `b` duas vezes em `1`. Depois disso:

```text
a = 5
b = 5
c = 4
```

Assim, o número total de bananas será:

```text
5 * 5 * 4 = 100
```

O objetivo é descobrir o maior valor possível de `a * b * c` depois de realizar
no máximo 5 operações.

## Entrada

A primeira linha contém um inteiro `t` (`1 <= t <= 1000`), o número de casos de
teste.

Cada caso de teste contém uma linha com três inteiros:

```text
a b c
```

com `1 <= a, b, c <= 10`.

## Saída

Para cada caso de teste, imprima um único inteiro: o maior produto possível após
as operações.

## Exemplo

Entrada:

```text
2
2 3 4
10 1 10
```

Saída:

```text
100
600
```

## Ideia da Solução

Como `a`, `b` e `c` são sempre positivos, aumentar qualquer um deles em `1`
nunca piora o produto. Por isso, apesar do enunciado dizer "no máximo 5 vezes",
sempre vale a pena usar exatamente as 5 operações.

Agora precisamos decidir como distribuir essas 5 operações entre os três
números.

Por exemplo, podemos fazer:

```text
0 operações em a, 0 em b, 5 em c
0 operações em a, 1 em b, 4 em c
0 operações em a, 2 em b, 3 em c
...
3 operações em a, 2 em b, 0 em c
...
5 operações em a, 0 em b, 0 em c
```

Para cada distribuição possível:

```text
x operações em a
y operações em b
z operações em c
```

com:

```text
x + y + z = 5
```

calculamos:

```text
(a + x) * (b + y) * (c + z)
```

e guardamos o maior valor encontrado.

Como existem poucas possibilidades, essa força bruta é suficiente.

## Complexidade

Para cada caso de teste, testamos todas as formas de distribuir 5 operações
entre 3 números.

Isso é constante e pequeno, então a complexidade por caso é:

```text
O(1)
```

