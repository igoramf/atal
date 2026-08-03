import sys
from collections import deque


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]
    indegree = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append(b)
        indegree[b] += 1

    fila = deque(i for i in range(n) if indegree[i] == 0)
    ordem = []

    while fila:
        vertice = fila.popleft()
        ordem.append(vertice)

        for vizinho in grafo[vertice]:
            indegree[vizinho] -= 1
            if indegree[vizinho] == 0:
                fila.append(vizinho)

    if len(ordem) != n:
        print("IMPOSSIBLE")
    else:
        print(*(vertice + 1 for vertice in ordem))


if __name__ == "__main__":
    main()
