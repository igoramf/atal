# Guia de Backtracking e Forca Bruta

Este guia resume os padroes principais para resolver questoes de backtracking e
forca bruta.

## 1. Ideia Central

Backtracking e uma forma organizada de testar possibilidades.

A estrutura mental e:

```text
estado atual
escolhas possiveis
faz uma escolha
chama a recursao
desfaz a escolha, se necessario
```

Modelo geral:

```python
def backtrack(estado):
    if caso_base:
        processa_resposta
        return

    for escolha in escolhas:
        if escolha_invalida:
            continue

        faz_escolha
        backtrack(novo_estado)
        desfaz_escolha
```

## 2. Perguntas Para Montar a Solucao

Antes de codar, responda:

```text
1. O que representa um estado da recursao?
2. Quando a recursao para?
3. Quais escolhas existem em cada nivel?
4. Quero contar todas as respostas ou encontrar uma?
5. A ordem das escolhas importa?
6. Preciso guardar o caminho?
7. Preciso desfazer alguma alteracao?
8. Existe alguma poda segura?
```

## 3. Caso Base

O caso base e quando uma possibilidade esta completa.

Exemplos:

```text
idx == n
len(path) == k
open_count == n and close_count == n
i == destino_i and j == destino_j
ops_restantes == 0
```

No caso base, voce geralmente:

```text
conta uma resposta
salva uma copia
atualiza melhor resposta
retorna True/False
```

## 4. Contar Tudo vs Encontrar Uma Solucao

Se o problema pede quantidade:

```text
nao pare na primeira solucao
continue explorando todos os ramos
```

Exemplo:

```python
if idx == n:
    if current_sum == target:
        count += 1
    return

backtrack(idx + 1, current_sum + nums[idx])
backtrack(idx + 1, current_sum - nums[idx])
```

Se o problema pede se existe uma solucao:

```text
pode retornar True assim que encontrar
```

Exemplo:

```python
if encontrou:
    return True

if backtrack(...):
    return True

return False
```

## 5. Quando Usar Dois Ramos

Use dois ramos quando cada item tem uma decisao binaria:

```text
pegar ou nao pegar
colocar + ou -
colocar no grupo 1 ou grupo 2
```

Padrao:

```python
def backtrack(idx, estado):
    if idx == n:
        processa
        return

    # escolhe nums[idx]
    backtrack(idx + 1, novo_estado_com_nums_idx)

    # nao escolhe nums[idx]
    backtrack(idx + 1, estado_sem_nums_idx)
```

Exemplos:

```text
subconjuntos
soma alvo
expressoes com + e -
dividir em dois grupos
```

## 6. Quando Usar Loop

Use `for` quando em cada nivel voce escolhe uma opcao entre varias.

Exemplos:

```text
escolher um caractere para a senha
escolher uma carta disponivel
escolher uma direcao no grid
escolher um item ainda nao usado
```

Padrao:

```python
for choice in choices:
    faz_escolha
    backtrack(...)
    desfaz_escolha
```

## 7. Permutacao vs Combinacao

Pergunta principal:

```text
[A, B] e diferente de [B, A]?
```

Se sim, e permutacao.

Se nao, e combinacao.

### Permutacao

A ordem importa.

Usa `used`.

```python
def backtrack(path, used):
    if len(path) == k:
        results.append(path[:])
        return

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        path.append(nums[i])

        backtrack(path, used)

        path.pop()
        used[i] = False
```

Exemplos:

```text
permutacoes de string
senhas sem repetir caracteres
ordem de jogadas
```

### Combinacao

A ordem nao importa.

Usa `start`.

```python
def backtrack(start, path):
    if len(path) == k:
        results.append(path[:])
        return

    for i in range(start, n):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

Exemplos:

```text
escolher time
escolher problemas
escolher subconjunto de tamanho k
```

## 8. Quando Usar `path[:]`

Use `path[:]` quando quiser salvar uma copia da lista atual.

```python
results.append(path[:])
```

Sem copia, voce salva a mesma lista mutavel, e ela muda depois com os `pop`.

Nao precisa de copia quando voce transforma em outro valor:

```python
results.append("".join(path))
results.append(sum(path))
results.append(tuple(path))
```

## 9. Quando Desfazer a Escolha

Desfaca quando voce modifica uma estrutura mutavel compartilhada:

```python
path.append(x)
backtrack(...)
path.pop()
```

```python
used[i] = True
backtrack(...)
used[i] = False
```

Nao precisa desfazer quando voce passa um novo valor:

```python
backtrack(idx + 1, current_sum + nums[idx])
backtrack(idx + 1, current_sum)
```

Inteiros, strings e tuplas sao imutaveis. Listas e matrizes sao mutaveis.

## 10. Poda

Poda e cortar um ramo que nao pode levar a resposta.

So use poda quando tiver certeza.

Exemplos seguros:

```python
if current_sum > target:
    return
```

Isso so e seguro se todos os numeros restantes forem positivos e voce nunca
puder diminuir a soma.

```python
if current_path >= best:
    return
```

Seguro em problemas de menor caminho com backtracking.

```python
if escolhidos + restantes < k:
    return
```

Seguro quando voce precisa escolher exatamente `k` itens.

Cuidado: em expressoes com `+` e `-`, esta poda nao e segura:

```python
if current_sum > target:
    return
```

Porque depois voce ainda pode subtrair.

## 11. Grid com Backtracking

Para grid, sempre pense:

```text
fora da matriz?
parede?
ja visitei?
cheguei no destino?
```

Com 4 direcoes, use `visited`.

```python
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def backtrack(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if grid[i][j] == "#":
        return False

    if visited[i][j]:
        return False

    if grid[i][j] == "E":
        return True

    visited[i][j] = True

    for di, dj in directions:
        if backtrack(i + di, j + dj):
            return True

    visited[i][j] = False
    return False
```

Se o movimento for apenas direita e baixo, geralmente nao precisa de `visited`,
porque nao ha ciclos.

## 12. Menor Caminho

Para menor caminho com backtracking:

```text
nao pare no primeiro caminho encontrado
explore todos os caminhos possiveis
atualize o melhor
use poda quando o caminho atual ja for pior que o melhor
```

Padrao:

```python
INF = float("inf")
best = INF

def backtrack(i, j, dist):
    nonlocal best

    if dist >= best:
        return

    if invalido:
        return

    if destino:
        best = min(best, dist)
        return

    marca_visitado

    for direcao in directions:
        backtrack(novo_i, novo_j, dist + 1)

    desmarca_visitado

return best if best != INF else -1
```

Observacao: para menor caminho em grade sem pesos, BFS costuma ser melhor que
backtracking. Mas backtracking serve para treinar busca e poda.

## 13. Parenteses Validos

Estado:

```text
path
open_count
close_count
```

Regras:

```text
pode abrir se open_count < n
pode fechar se close_count < open_count
termina quando open_count == n and close_count == n
```

Padrao:

```python
def backtrack(path, open_count, close_count):
    if open_count == n and close_count == n:
        results.append("".join(path))
        return

    if open_count < n:
        path.append("(")
        backtrack(path, open_count + 1, close_count)
        path.pop()

    if close_count < open_count:
        path.append(")")
        backtrack(path, open_count, close_count + 1)
        path.pop()
```

## 14. Erros Comuns

```text
esquecer de chamar o backtrack inicial
esquecer return no caso base
usar return True quando precisa contar todas as respostas
nao desfazer path ou visited
usar used quando precisava de start
usar start quando precisava de used
validar antes de completar a solucao
podar com uma condicao que nao e sempre segura
salvar path sem copia
começar grid sempre em (0, 0) quando precisa procurar S
ignorar indices negativos em grid com 4 direcoes
```

## 15. Checklist Antes de Entregar

Use esta lista:

```text
[ ] Eu sei o que cada chamada recursiva representa?
[ ] O caso base esta correto?
[ ] O caso base tem return?
[ ] Estou contando tudo ou parando cedo corretamente?
[ ] A ordem importa? Usei used ou start corretamente?
[ ] Se usei path, fiz append/pop balanceados?
[ ] Se salvei path, usei copia?
[ ] Se usei visited, marquei e desmarquei corretamente?
[ ] Minha poda e realmente segura?
[ ] Testei caso pequeno?
[ ] Testei caso sem solucao?
[ ] Testei caso com varias solucoes?
```

