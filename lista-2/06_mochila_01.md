# 6. Mochila 0/1

Voce tem `n` itens. Cada item tem peso `w[i]` e valor `v[i]`. Sua mochila suporta no maximo peso `W`.

Cada item pode ser escolhido no maximo uma vez. Determine o maior valor total possivel sem ultrapassar a capacidade.

## Entrada

```text
n W
w1 v1
w2 v2
...
wn vn
```

## Saida

```text
maior valor possivel
```

## Exemplo

```text
Entrada:
5 9
2 40
3 50
5 100
4 95
3 30

Saida:
195
```

## Classificacao

Branch and Bound.
