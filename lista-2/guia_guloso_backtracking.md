# Guia: Algoritmos Gulosos e Backtracking

Este guia serve para reconhecer, pensar e implementar problemas de guloso e backtracking.

## 1. Algoritmos Gulosos

Um algoritmo guloso constroi a resposta fazendo a melhor escolha local em cada passo e nunca volta atras.

Ideia central:

```text
escolher o melhor agora
fixar a escolha
continuar o problema menor
```

Para um problema ser guloso, a escolha local precisa ser segura. Ou seja, deve existir uma solucao otima que inclui essa escolha.

### Checklist para identificar guloso

Pergunte:

```text
1. O problema pede minimizar ou maximizar algo?
2. Existe uma escolha local que parece claramente melhor?
3. Essa escolha nao prejudica o futuro?
4. Depois da escolha, sobra um problema parecido?
5. Eu consigo justificar que uma solucao otima pode usar essa escolha?
```

Se sim, provavelmente e guloso.

### Padrao 1: ordenar e escolher

Muito comum em problemas gulosos.

Formato:

```python
itens.sort(key=criterio)

resposta = 0
estado = estado_inicial

for item in itens:
    if item_pode_ser_escolhido(item, estado):
        escolhe(item)
        atualiza_estado()
```

Exemplos:

```text
Selecao de atividades -> ordenar pelo tempo de fim
Mochila fracionaria -> ordenar por valor/peso
Kruskal -> ordenar arestas por peso
```

### Exemplo: selecao de atividades

Problema:

```text
Escolher o maior numero de atividades sem sobreposicao.
```

Criterio guloso:

```text
escolher a atividade que termina mais cedo
```

Por que funciona?

```text
Uma atividade que termina mais cedo deixa mais espaco para atividades futuras.
```

Molde:

```python
atividades.sort(key=lambda atividade: atividade[1])

count = 0
ultimo_fim = -1

for inicio, fim in atividades:
    if inicio >= ultimo_fim:
        count += 1
        ultimo_fim = fim
```

### Padrao 2: manter o melhor visto ate agora

Quando a ordem da entrada importa, talvez voce nao ordene. Em vez disso, guarda a melhor opcao disponivel ate aquele momento.

Exemplo: compra de carne.

```text
Para comer no dia i, posso usar carne comprada em qualquer dia de 1 ate i.
Logo, o melhor preco para o dia i e o menor preco visto ate agora.
```

Molde:

```python
melhor = infinito
resposta = 0

for quantidade, preco in dias:
    melhor = min(melhor, preco)
    resposta += quantidade * melhor
```

### Padrao 3: avancar o maximo possivel

Exemplo: reabastecimento minimo.

```text
De todos os postos alcancaveis, escolha o mais distante.
```

Esse tipo de guloso tenta reduzir o numero de decisoes futuras.

### Padrao 4: heap de melhor opcao disponivel

Alguns gulosos usam fila de prioridade.

Formato:

```python
heap = []

for evento in eventos:
    adiciona_opcoes_disponiveis(heap, evento)
    melhor = heappop(heap)
    usa(melhor)
```

Exemplos:

```text
Huffman -> junta sempre os dois menores pesos
Escalonamento com prazos e lucros -> escolhe maior lucro disponivel
```

### Quando desconfiar que nao e guloso

Desconfie se:

```text
uma escolha local pode bloquear uma solucao melhor
voce precisa testar pegar ou nao pegar varias opcoes
o problema pede contar todas as solucoes
o problema pede verificar se existe alguma combinacao
existem subproblemas repetidos
```

Nesses casos, pode ser:

```text
programacao dinamica
backtracking
branch and bound
forca bruta
```

---

## 2. Backtracking

Backtracking e uma busca em profundidade que constroi uma solucao passo a passo. Quando percebe que o caminho atual nao pode gerar uma resposta valida, ele volta e tenta outra escolha.

Ideia central:

```text
escolhe
explora
desfaz
tenta outra escolha
```

Backtracking e usado quando voce precisa:

```text
gerar todas as solucoes
contar solucoes validas
verificar se existe uma configuracao valida
resolver problemas combinatorios
```

### Checklist para identificar backtracking

Pergunte:

```text
1. Estou construindo uma solucao por partes?
2. Em cada etapa existem varias escolhas possiveis?
3. Preciso testar combinacoes?
4. Posso abandonar um caminho assim que ele fica invalido?
5. Preciso desfazer escolhas para tentar outras?
```

Se sim, provavelmente e backtracking.

### Molde geral

```python
def backtrack(estado):
    if estado_completo(estado):
        processa_solucao(estado)
        return

    for escolha in escolhas_possiveis(estado):
        if escolha_e_valida(escolha, estado):
            aplica(escolha, estado)
            backtrack(estado)
            desfaz(escolha, estado)
```

### Padrao 1: gerar sequencias

Exemplo: gerar parenteses.

Estado:

```text
sequencia atual
quantidade de "(" usados
quantidade de ")" usados
```

Regras:

```text
posso abrir se abertos < n
posso fechar se fechados < abertos
```

Molde:

```python
def backtrack(atual, abertos, fechados):
    if len(atual) == 2 * n:
        resposta.append(atual)
        return

    if abertos < n:
        backtrack(atual + "(", abertos + 1, fechados)

    if fechados < abertos:
        backtrack(atual + ")", abertos, fechados + 1)
```

### Padrao 2: permutacoes com restricao

Exemplo: arranjo bonito.

Estado:

```text
posicao atual
numeros usados
quantidade de respostas
```

Regra:

```text
num % pos == 0 ou pos % num == 0
```

Molde:

```python
def backtrack(pos):
    if pos > n:
        resposta += 1
        return

    for num in range(1, n + 1):
        if not usado[num] and regra_valida(pos, num):
            usado[num] = True
            backtrack(pos + 1)
            usado[num] = False
```

### Padrao 3: distribuir itens em grupos

Exemplo: particionar em `k` subconjuntos com soma igual.

Estado:

```text
indice do item atual
soma atual de cada grupo
```

Poda:

```text
nao colocar item em grupo que ultrapassa o alvo
evitar testar grupos vazios equivalentes
ordenar itens decrescente para falhar cedo
```

Isso nao e guloso: ordenar ajuda a busca, mas nao define uma escolha definitiva.

### Poda em backtracking

Poda e qualquer regra que evita explorar caminhos impossiveis ou repetidos.

Exemplos:

```text
parenteses: nao fechar se nao existe abertura disponivel
arranjo bonito: nao colocar numero que viola a divisibilidade
k subconjuntos: nao passar da soma alvo
```

Boa poda deixa o algoritmo muito mais rapido.

---

## 3. Guloso vs Backtracking

## Guloso

```text
faz uma escolha local
nao volta atras
normalmente busca uma resposta otima
precisa de prova de escolha segura
costuma ser rapido
```

Exemplo:

```text
Selecao de atividades: escolhe a que termina mais cedo.
```

## Backtracking

```text
testa varias escolhas
volta atras
gera, conta ou procura configuracoes validas
usa poda para evitar caminhos ruins
pode ser exponencial
```

Exemplo:

```text
Gerar parenteses: tenta abrir e fechar respeitando as regras.
```

## Como decidir

Se voce pensa:

```text
sei exatamente qual escolha local fazer agora e ela e segura
```

provavelmente e guloso.

Se voce pensa:

```text
preciso tentar possibilidades diferentes e voltar quando der errado
```

provavelmente e backtracking.

---

## 4. Frases mentais uteis

Para guloso:

```text
Qual escolha local e segura?
Qual criterio de ordenacao faz sentido?
Depois de escolher, o problema restante continua igual?
Consigo trocar uma solucao otima por outra que usa minha escolha?
```

Para backtracking:

```text
Qual e o estado?
Quais escolhas existem agora?
Quando uma solucao esta completa?
Quando uma escolha e invalida?
Como desfaco a escolha?
Qual poda posso aplicar?
```

---

## 5. Classificacao dos problemas vistos

```text
Duff e Carne -> guloso
Selecao de Atividades -> guloso
Robin Hood -> simulacao/ad hoc
Maquina Estranha -> simulacao/ad hoc
Gerar Parenteses -> backtracking
Arranjo Bonito -> backtracking com poda
Particao em K Subconjuntos -> backtracking com poda
Wildcard Matching -> programacao dinamica
Alocacao de Tarefas -> Branch and Bound
Mochila 0/1 -> Branch and Bound
```
