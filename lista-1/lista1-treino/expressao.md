# E. Expressao

## Enunciado

Petya estuda na escola e adora matematica. A turma dele esta estudando
expressoes aritmeticas.

Na ultima aula, o professor escreveu tres inteiros positivos `a`, `b` e `c` no
quadro. A tarefa era inserir os sinais de operacao `+` e `*` e, se quiser,
parenteses entre os numeros, de modo que o valor da expressao seja o maior
possivel.

Por exemplo, suponha que o professor tenha escrito os numeros `1`, `2` e `3` no
quadro. Algumas formas de colocar sinais e parenteses:

```text
1 + 2 * 3 = 7
1 * (2 + 3) = 5
1 * 2 * 3 = 6
(1 + 2) * 3 = 9
```

Observe que voce so pode inserir sinais de operacao entre `a` e `b`, e entre
`b` e `c`. Ou seja, nao e permitido trocar a ordem dos numeros.

Por exemplo, no caso acima, nao e possivel obter a expressao:

```text
(1 + 3) * 2
```

E facil ver que o valor maximo que se pode obter no exemplo e `9`.

Sua tarefa e: dados `a`, `b` e `c`, imprimir o valor maximo que se pode obter.

## Entrada

A entrada contem tres inteiros `a`, `b` e `c`, cada um em uma linha.

```text
1 <= a, b, c <= 10
```

## Saida

Imprima o valor maximo da expressao que voce pode obter.

## Exemplos

Exemplo 1:

Entrada:

```text
1
2
3
```

Saida:

```text
9
```

Exemplo 2:

Entrada:

```text
2
10
3
```

Saida:

```text
60
```

