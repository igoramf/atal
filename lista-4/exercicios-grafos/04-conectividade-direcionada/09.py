import sys


def alcancaveis(grafo, inicio):
    visitado = [False] * len(grafo)
    visitado[inicio] = True
    pilha = [inicio]

    while pilha:
        vertice = pilha.pop()
        for vizinho in grafo[vertice]:
            if not visitado[vizinho]:
                visitado[vizinho] = True
                pilha.append(vizinho)

    return visitado


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

    visitado = alcancaveis(grafo, 0)
    for vertice in range(n):
        if not visitado[vertice]:
            print("NO")
            print(1, vertice + 1)
            return

    visitado = alcancaveis(reverso, 0)
    for vertice in range(n):
        if not visitado[vertice]:
            print("NO")
            print(vertice + 1, 1)
            return

    print("YES")


if __name__ == "__main__":
    main()
