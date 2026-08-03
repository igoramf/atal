import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append(b)
        grafo[b].append(a)

    visitado = [False] * n
    representantes = []

    for inicio in range(n):
        if visitado[inicio]:
            continue

        representantes.append(inicio)
        visitado[inicio] = True
        pilha = [inicio]

        while pilha:
            vertice = pilha.pop()
            for vizinho in grafo[vertice]:
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    pilha.append(vizinho)

    print(len(representantes) - 1)
    for i in range(1, len(representantes)):
        print(representantes[i - 1] + 1, representantes[i] + 1)


if __name__ == "__main__":
    main()
