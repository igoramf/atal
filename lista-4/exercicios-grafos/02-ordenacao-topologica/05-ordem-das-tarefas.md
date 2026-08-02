# 05 - Ordem das tarefas

## Tema

Ordenação topológica, grau de entrada e algoritmo de Kahn.

## Problema

Existem `n` tarefas e `m` dependências. Uma dependência `a b` informa que a tarefa `a` precisa terminar antes da tarefa `b`. Encontre uma ordem válida para executar todas as tarefas.

## Entrada

- `n m`: número de tarefas e dependências.
- `m` linhas com `a b`, representando a aresta dirigida `a -> b`.

## Saída

Imprima uma ordenação válida ou `IMPOSSIBLE` caso exista ciclo.

## Exemplo

```text
Entrada
4 4
1 3
2 3
3 4
1 4

Saída possível
1 2 3 4
```

## Dicas graduais

1. Para cada aresta `a -> b`, aumente o grau de entrada de `b`.
2. Coloque na fila todos os vértices com grau de entrada zero.
3. Se a resposta tiver menos de `n` vértices, existe um ciclo.

## Meta

Implementar o algoritmo de Kahn sem consultar o arquivo de exemplo.

