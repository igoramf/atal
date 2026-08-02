from collections import deque

def solve(n, arestas):
    grafo = [[] for _ in range(n)]
    indegree = [0] * n

    for origem, destino in arestas:
        indegree[destino] += 1
        grafo[origem].append(destino)

    fila = deque()

    for vertice in range(n):
        if indegree[vertice] == 0:
            fila.append(vertice)

    ordem = []

    while fila:

        vertice = fila.popleft()
        ordem.append(vertice)

        for vizinho in grafo[vertice]:
            indegree[vizinho] -= 1

            if indegree[vizinho] == 0:
                fila.append(vizinho)

    if len(ordem) != n:
        return None

    return ordem




def main():
    n, m = map(int, input().split())
    arestas = []
    for _ in range(m):
        x, y = map(int, input().split())
        arestas.append((x - 1, y - 1))

    ordem = solve(n, arestas)

    if ordem is None:
        print("IMPOSSIBLE")
    else:
        print(*(vertice + 1 for vertice in ordem))


if __name__ == '__main__':
    main()
