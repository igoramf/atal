# Guia: Divisao e Conquista e Programacao Dinamica

## 1. Divisao e conquista

Divisao e conquista resolve um problema quebrando-o em partes menores,
resolvendo cada parte e combinando os resultados.

Formato comum:

```python
def solve(l, r):
    if caso_base:
        return resposta_simples

    mid = (l + r) // 2
    left = solve(l, mid)
    right = solve(mid + 1, r)
    return combina(left, right)
```

Checklist:

```text
1. Consigo dividir a entrada em duas ou mais partes?
2. Cada parte parece o mesmo problema original?
3. Existe um caso base pequeno?
4. Depois de resolver as partes, consigo combinar as respostas?
```

Exemplos classicos:

```text
busca binaria
merge sort
contagem de inversoes
exponenciacao rapida
subarray maximo por divisao e conquista
```

## 2. Programacao dinamica

Programacao dinamica resolve problemas com subproblemas repetidos e estrutura
otima. Em vez de recalcular, guarda respostas em uma tabela.

Perguntas principais:

```text
1. Qual e o estado?
2. O que dp[estado] representa?
3. Qual e a transicao?
4. Quais sao os casos base?
5. Qual ordem garante que as dependencias ja foram calculadas?
```

Molde bottom-up:

```python
dp = inicializa_tabela()

for estado in ordem:
    dp[estado] = melhor_resposta_usando_estados_anteriores

print(dp[estado_final])
```

Molde top-down:

```python
from functools import lru_cache

@lru_cache(None)
def solve(estado):
    if caso_base:
        return resposta
    return combina_chamadas_menores()
```

## Como diferenciar

Use divisao e conquista quando:

```text
os subproblemas sao independentes
voce divide, resolve e combina
nao ha muito recalculo entre ramos
```

Use programacao dinamica quando:

```text
as mesmas chamadas aparecem varias vezes
uma decisao depende de resultados anteriores
voce precisa maximizar, minimizar ou contar formas
```

## Padroes de DP mais comuns

```text
1D:
dp[i] = resposta considerando prefixo ate i

2D:
dp[i][j] = resposta considerando os i primeiros itens e capacidade j

Strings:
dp[i][j] = resposta entre prefixos s[:i] e t[:j]

Grade:
dp[i][j] = resposta para chegar na celula (i, j)
```
