import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]
    reverso = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append(b)
        reverso[b].append(a)

    visitado = [False] * n
    ordem = []

    for inicio in range(n):
        if visitado[inicio]:
            continue

        pilha = [(inicio, False)]
        while pilha:
            vertice, finalizando = pilha.pop()

            if finalizando:
                ordem.append(vertice)
                continue
            if visitado[vertice]:
                continue

            visitado[vertice] = True
            pilha.append((vertice, True))
            for vizinho in grafo[vertice]:
                if not visitado[vizinho]:
                    pilha.append((vizinho, False))

    componente = [0] * n
    quantidade = 0

    for inicio in reversed(ordem):
        if componente[inicio] != 0:
            continue

        quantidade += 1
        componente[inicio] = quantidade
        pilha = [inicio]

        while pilha:
            vertice = pilha.pop()
            for vizinho in reverso[vertice]:
                if componente[vizinho] == 0:
                    componente[vizinho] = quantidade
                    pilha.append(vizinho)

    print(quantidade)
    print(*componente)


if __name__ == "__main__":
    main()
