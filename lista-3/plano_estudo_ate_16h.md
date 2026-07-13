# Plano de estudo ate 16h

Contexto: em 13/07/2026, eram 12:53 no momento em que esta lista foi criada.
O objetivo e revisar padroes que ajudam a reconhecer e implementar solucoes
rapidamente.

## 12:55 - 13:20: reconhecer os dois temas

Leia:

```text
guia_divisao_conquista_programacao_dinamica.md
```

Foque em responder:

```text
Quando eu divido em subproblemas independentes?
Quando eu tenho subproblemas repetidos?
Como escrever a recorrencia?
Qual e o estado da DP?
```

## 13:20 - 14:05: divisao e conquista

Faca nesta ordem:

```text
01_busca_binaria
02_contar_inversoes
04_exponenciacao_rapida
05_subarray_maximo_divisao_conquista
```

Prioridade:

```text
entender caso base
entender chamada recursiva
entender combinacao das respostas
```

## 14:05 - 15:20: programacao dinamica

Faca nesta ordem:

```text
06_fibonacci_dp
09_troco_minimo_dp
07_mochila_01_dp
08_lcs
10_caminhos_grade_obstaculos
```

Prioridade:

```text
definir estado
definir transicao
definir inicializacao
definir ordem de preenchimento
```

## 15:20 - 15:50: refazer sem olhar

Refaca pelo menos:

```text
02_contar_inversoes
07_mochila_01_dp
08_lcs
```

## 15:50 - 16:00: revisao final

Decore estes moldes:

```text
Divisao e conquista:
resolver(l, r)
caso base
mid = (l + r) // 2
resposta esquerda
resposta direita
combinar

Programacao dinamica:
dp[estado] = resposta para aquele estado
inicializar casos base
preencher em ordem que dependencias ja existam
responder com dp[estado_final]
```
