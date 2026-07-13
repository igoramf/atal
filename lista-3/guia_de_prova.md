# Guia de prova: Divisao e Conquista e Programacao Dinamica

Este guia e para usar durante a prova, quando aparecer um problema novo e voce
precisar decidir rapidamente como atacar.

## 1. Primeiro minuto: classifique o problema

Leia o enunciado e pergunte:

```text
O problema pede procurar em vetor ordenado?
-> provavelmente busca binaria.

O problema divide naturalmente a entrada em metade esquerda e metade direita?
-> provavelmente divisao e conquista.

O problema pede maior, menor, quantidade de formas ou possibilidade?
-> pode ser programacao dinamica.

Uma escolha local pode bloquear uma resposta melhor?
-> desconfie de guloso; tente DP.

As mesmas decisoes aparecem de novo em varios caminhos?
-> programacao dinamica.

Tenho itens que posso pegar ou nao pegar?
-> mochila / subset sum / DP 0-1.

Tenho duas strings?
-> DP 2D em prefixos.

Tenho grade e movimentos limitados?
-> DP em celulas.
```

## 2. Receita para divisao e conquista

Use quando o problema tem este formato:

```text
resolver intervalo
dividir no meio
resolver esquerda
resolver direita
combinar
```

Molde:

```python
def solve(l, r):
    if l == r:
        return caso_base

    mid = (l + r) // 2
    left = solve(l, mid)
    right = solve(mid + 1, r)
    return combine(left, right)
```

Checklist antes de escrever:

```text
1. Qual e o caso base?
2. O que a funcao retorna?
3. Como divido a entrada?
4. Como combino as respostas?
```

Exemplos:

```text
Busca binaria:
combinacao quase nao existe; escolhe so um lado.

Merge sort:
combina intercalando ordenado.

Contar inversoes:
inversoes = esquerda + direita + inversoes cruzadas.

Subarray maximo:
resposta = max(esquerda, direita, melhor cruzando o meio).

Exponenciacao rapida:
a^b = (a^(b//2))^2, multiplicando por a se b for impar.
```

## 3. Receita para programacao dinamica

Se o problema for DP, nao comece pelo codigo. Comece por estas 4 linhas:

```text
Estado:
dp[...] significa:
Transicao:
Resposta final:
```

Exemplo para mochila:

```text
Estado:
dp[c]

dp[c] significa:
maior valor usando itens ja processados com capacidade c

Transicao:
dp[c] = max(dp[c], dp[c - peso] + valor)

Resposta final:
dp[W]
```

## 4. Como descobrir o estado da DP

Procure o que muda nas escolhas.

```text
Escolho entre itens?
-> estado geralmente usa indice do item e capacidade/soma.

Estou comparando duas strings?
-> estado usa i e j.

Estou andando em grade?
-> estado usa linha e coluna.

Estou formando valor com moedas?
-> estado usa valor atual.

Estou contando formas ate posicao i?
-> estado usa i.
```

## 5. Transicoes mais comuns

### Pegar ou nao pegar

Usado em mochila, subset sum, escolher elementos.

```python
nao_pega = dp[i - 1][c]
pega = dp[i - 1][c - peso] + valor
dp[i][c] = max(nao_pega, pega)
```

Com vetor 1D para mochila 0/1:

```python
for peso, valor in itens:
    for c in range(W, peso - 1, -1):
        dp[c] = max(dp[c], dp[c - peso] + valor)
```

Importante:

```text
0/1 -> percorre capacidade de tras para frente.
Ilimitado -> percorre capacidade de frente para tras.
```

### Minimo numero de moedas

```python
dp[0] = 0
dp[x] = infinito

for x in range(1, S + 1):
    for moeda in moedas:
        if moeda <= x:
            dp[x] = min(dp[x], dp[x - moeda] + 1)
```

### Duas strings

```python
if a[i - 1] == b[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

### Grade

```python
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

Se tiver obstaculo:

```python
if grid[i][j] == "#":
    dp[i][j] = 0
```

## 6. Erros comuns em prova

```text
Esquecer caso base.
Usar indice negativo sem querer.
Criar dp com tamanho n em vez de n + 1.
Confundir capacidade 0/1 com ilimitada.
Percorrer mochila 0/1 de frente para tras.
Nao inicializar infinito em problemas de minimo.
Retornar dp errado no final.
Nao testar o exemplo manualmente.
```

## 7. Como testar rapido no papel

Depois de escrever, teste:

```text
menor caso possivel
caso do exemplo
caso com resposta zero/impossivel
caso com um unico elemento
caso em que escolher o primeiro parece bom mas nao e
```

## 8. Frases que denunciam DP

```text
"maior valor possivel"
"menor custo"
"quantas formas"
"subsequencia"
"prefixos"
"capacidade"
"soma alvo"
"caminhos"
"pode ou nao escolher"
"cada item no maximo uma vez"
```

## 9. Frases que denunciam divisao e conquista

```text
"vetor ordenado"
"metade"
"intervalo"
"pares i < j"
"combinar resultados"
"potencia grande"
"ordenar"
```

## 10. Decisao final se travar

Se estiver travado, escolha este caminho:

```text
1. Escreva uma solucao recursiva simples.
2. Veja quais parametros mudam.
3. Esses parametros viram o estado.
4. Coloque cache ou transforme em tabela.
5. Otimize so se sobrar tempo.
```

Para prova, uma DP top-down com `lru_cache` muitas vezes e mais facil de
escrever corretamente do que uma tabela bottom-up.

Molde top-down:

```python
from functools import lru_cache

@lru_cache(None)
def solve(i, estado):
    if caso_base:
        return resposta

    return melhor_entre_opcoes
```
