# Guia: Algoritmos Gulosos e Branch and Bound

Este guia serve para reconhecer, pensar e implementar os dois grupos desta lista:

```text
Questoes 1-5  -> algoritmos gulosos
Questoes 6-10 -> branch and bound
```

Observacao: se a numeracao da disciplina estiver de 0 a 10, a ideia e a mesma: a primeira metade e gulosa, e a segunda metade e Branch and Bound.

---

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

Exemplos desta lista:

```text
Selecao de atividades -> ordenar pelo tempo de fim
Mochila fracionaria -> ordenar por valor/peso
Troco canonico -> escolher a maior moeda possivel
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
voce precisa comparar muitas combinacoes completas
voce consegue calcular um limite otimista para podar ramos
```

Nesses casos, pode ser:

```text
programacao dinamica
branch and bound
forca bruta
```

---

## 2. Branch and Bound

Branch and Bound e uma busca em arvore para problemas de otimizacao. Ele testa escolhas possiveis, mas evita explorar ramos que nao conseguem melhorar a melhor resposta ja encontrada.

Ideia central:

```text
branch -> dividir o problema em escolhas/filhos
bound  -> calcular um limite otimista para cada filho
poda   -> ignorar filhos que nao podem bater a melhor resposta atual
```

Branch and Bound e usado quando voce precisa:

```text
minimizar ou maximizar uma funcao objetivo
resolver um problema combinatorio
testar combinacoes sem necessariamente testar todas
manter a melhor solucao encontrada ate agora
calcular um limite otimista para cada solucao parcial
```

### Checklist para identificar Branch and Bound

Pergunte:

```text
1. O problema pede a melhor solucao, nao apenas qualquer solucao?
2. A solucao e formada por varias decisoes combinatorias?
3. Uma escolha local pode atrapalhar a resposta global?
4. Eu consigo representar uma solucao parcial como um no?
5. Eu consigo estimar o melhor resultado possivel a partir desse no?
6. Se essa estimativa ja for pior que a melhor resposta atual, posso podar?
```

Se sim, provavelmente e Branch and Bound.

### Conceitos principais

```text
No
Uma solucao parcial.

Branch
Gerar filhos a partir de novas escolhas.

Bound
Limite otimista do melhor resultado que aquele ramo ainda pode atingir.

Best
Melhor solucao completa encontrada ate agora.

Poda
Descartar um no cujo bound nao consegue melhorar best.
```

Para minimizacao:

```text
bound = menor custo possivel estimado daquele ramo
poda se bound >= best_cost
```

Para maximizacao:

```text
bound = maior valor possivel estimado daquele ramo
poda se bound <= best_value
```

### Molde geral com fila de prioridade

```python
heap = []
best = resposta_ruim

root = cria_no_inicial()
root.bound = calcula_bound(root)
heappush(heap, root)

while heap:
    node = heappop(heap)

    if nao_pode_melhorar(node.bound, best):
        continue

    if solucao_completa(node):
        best = atualiza_best(best, node)
        continue

    for child in gera_filhos(node):
        child.bound = calcula_bound(child)

        if pode_melhorar(child.bound, best):
            heappush(heap, child)
```

A fila de prioridade faz o algoritmo visitar primeiro o no mais promissor.

```text
minimizacao -> menor bound primeiro
maximizacao -> maior bound primeiro
```

Em Python, `heapq` e min-heap. Para maximizar, e comum usar `priority = -bound`.

---

## 3. Padroes de Branch and Bound nesta lista

### 6. Mochila 0/1

Objetivo:

```text
maximizar valor sem ultrapassar a capacidade
```

Branch:

```text
para cada item, gerar dois filhos:
pegar o item
nao pegar o item
```

Bound:

```text
valor atual + estimativa otimista usando mochila fracionaria
```

Por que o bound e otimista?

```text
A mochila 0/1 nao pode pegar pedacos de item.
Se eu permito pegar fracao do proximo item, estou relaxando o problema.
Logo, a estimativa fica pelo menos tao boa quanto qualquer solucao real daquele ramo.
```

Poda:

```text
se bound <= best_value, descarta o ramo
se peso atual > capacidade, descarta o ramo
```

### 7. Alocacao de tarefas

Objetivo:

```text
minimizar o custo de atribuir n tarefas a n trabalhadores
```

Branch:

```text
no nivel i, escolher qual tarefa ainda livre vai para o trabalhador i
```

Bound:

```text
custo atual
+ menor custo possivel para cada trabalhador restante,
  ignorando conflitos futuros entre algumas escolhas
```

Poda:

```text
se bound >= best_cost, descarta o ramo
```

### 8. Caixeiro viajante

Objetivo:

```text
minimizar o custo de um ciclo que sai da cidade 0,
visita todas as cidades uma vez e volta para 0
```

Branch:

```text
escolher a proxima cidade ainda nao visitada
```

Bound:

```text
custo parcial do caminho
+ estimativa minima para conectar as cidades restantes
+ estimativa para conseguir voltar ao inicio
```

Exemplos de bounds comuns:

```text
menor aresta de saida para cada cidade restante
reducao de matriz de custos
estimativa baseada nas duas menores arestas por cidade
```

Poda:

```text
se bound >= best_tour, descarta o ramo
```

### 9. Escalonamento em duas maquinas

Objetivo:

```text
minimizar o maior tempo final entre as duas maquinas
```

Branch:

```text
para cada tarefa, gerar dois filhos:
colocar na maquina A
colocar na maquina B
```

Bound:

```text
o makespan final nunca pode ser menor que:
maior carga atual entre as duas maquinas
metade da soma total das tarefas
```

Um bound simples:

```python
bound = max(carga_a, carga_b, ceil(soma_total / 2))
```

Poda:

```text
se bound >= best_makespan, descarta o ramo
```

### 10. Clique maxima

Objetivo:

```text
maximizar o tamanho de uma clique
```

Branch:

```text
escolher incluir ou nao incluir vertices candidatos
```

Estado comum:

```text
clique atual
candidatos que ainda podem entrar na clique
```

Bound:

```text
tamanho da clique atual + quantidade de candidatos restantes
```

Esse bound e otimista porque, no melhor caso, todos os candidatos restantes poderiam entrar.

Poda:

```text
se len(clique_atual) + len(candidatos) <= best_size, descarta o ramo
```

---

## 4. Guloso vs Branch and Bound

## Guloso

```text
faz uma escolha local definitiva
nao volta atras
precisa de prova de escolha segura
costuma ser rapido
normalmente tem complexidade polinomial
```

Exemplo:

```text
Selecao de atividades: escolhe a atividade que termina mais cedo.
```

## Branch and Bound

```text
testa varias escolhas
mantem a melhor solucao completa encontrada
usa bound otimista para podar ramos
resolve problemas de otimizacao combinatoria
pode continuar sendo exponencial no pior caso
```

Exemplo:

```text
Mochila 0/1: tenta pegar ou nao pegar itens, mas poda ramos cujo bound fracionario nao supera o melhor valor atual.
```

## Como decidir

Se voce pensa:

```text
sei exatamente qual escolha local fazer agora e ela e segura
```

provavelmente e guloso.

Se voce pensa:

```text
preciso testar possibilidades diferentes,
mas consigo calcular um limite otimista para cortar ramos ruins
```

provavelmente e Branch and Bound.

---

## 5. Frases mentais uteis

Para guloso:

```text
Qual escolha local e segura?
Qual criterio de ordenacao faz sentido?
Depois de escolher, o problema restante continua igual?
Consigo trocar uma solucao otima por outra que usa minha escolha?
```

Para Branch and Bound:

```text
Qual e o estado de uma solucao parcial?
Quais filhos esse no gera?
O problema e de minimizacao ou maximizacao?
Qual e a melhor solucao completa encontrada ate agora?
Qual bound otimista eu consigo calcular?
Quando esse bound prova que o ramo nao vale a pena?
Qual no deve ser explorado primeiro?
```

---

## 6. Classificacao dos problemas desta lista

```text
1. Compra de Carne                 -> guloso
2. Selecao de Atividades           -> guloso
3. Troco Canonico                  -> guloso
4. Mochila Fracionaria             -> guloso
5. Reabastecimento Minimo          -> guloso
6. Mochila 0/1                     -> Branch and Bound
7. Alocacao de Tarefas             -> Branch and Bound
8. Caixeiro Viajante               -> Branch and Bound
9. Escalonamento em Duas Maquinas  -> Branch and Bound
10. Clique Maxima                  -> Branch and Bound
```
