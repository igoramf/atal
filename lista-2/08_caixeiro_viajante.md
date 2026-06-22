# 8. Caixeiro Viajante

Voce tem `n` cidades e uma matriz de distancias `d[i][j]`. Um vendedor comeca na cidade `0`, visita todas as outras cidades exatamente uma vez e retorna para a cidade `0`.

Determine a menor distancia total possivel.

## Entrada

```text
n
d11 d12 ... d1n
d21 d22 ... d2n
...
dn1 dn2 ... dnn
```

## Saida

```text
menor ciclo possivel
```

## Exemplo

```text
Entrada:
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0

Saida:
80
```

## Classificacao

Branch and Bound.
