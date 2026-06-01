# C. Anos com Digitos Diversos

## Enunciado

Parece que o ano de 2013 chegou apenas ontem. Voce sabia de um fato curioso?
O ano de 2013 e o primeiro ano depois de 1987 que possui todos os digitos
distintos.

Agora, voce deve resolver o seguinte problema: dado um ano, encontre o menor
ano que seja estritamente maior que o ano fornecido e que tenha todos os
digitos diferentes entre si.

## Entrada

A unica linha contem um inteiro `y` (`1000 <= y <= 9000`), o numero do ano.

## Saida

Imprima um unico inteiro: o menor ano que seja estritamente maior que `y` e
cujos digitos sejam todos distintos.

E garantido que a resposta existe.

## Exemplos

Exemplo 1:

Entrada:

```text
1987
```

Saida:

```text
2013
```

Exemplo 2:

Entrada:

```text
2013
```

Saida:

```text
2014
```

## Ideia da Solucao

A ideia e testar os anos candidatos em ordem crescente.

Comecamos em `y + 1`, porque o ano precisa ser estritamente maior que `y`.
Depois, verificamos se todos os digitos desse ano sao distintos.

Se forem, encontramos a resposta. Como estamos testando em ordem crescente, o
primeiro ano valido encontrado ja e o menor possivel.

Para verificar se os digitos sao distintos, podemos transformar o ano em string
e comparar:

```text
quantidade de digitos do ano
quantidade de digitos diferentes do ano
```

Se as duas quantidades forem iguais, todos os digitos sao distintos.

## Complexidade

Como `y <= 9000` e o ano tem apenas 4 digitos, a busca e pequena.

Na pratica, a solucao roda em tempo constante para os limites do problema.

