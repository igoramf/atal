import heapq

def solve(n, arestas):
    grafo = [[] for _ in range(n)]

    for origem, destino, custo in arestas:
        grafo[origem].append((destino, custo))

    distancia = [float("inf")] * n
    distancia[0] = 0
    fila = [(0, 0)]

    while fila:
        distancia_atual, vertice = heapq.heappop(fila)

        if distancia_atual > distancia[vertice]:
            continue

        for vizinho, custo in grafo[vertice]:
            nova_distancia = distancia_atual + custo

            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancia

def main():
    n, m = map(int, input().split())
    arestas = []
    for _ in range(m):
        x, y, c = map(int, input().split())
        if c < 0:
            raise ValueError("Dijkstra nao aceita custos negativos.")
        arestas.append((x - 1, y - 1, c))

    distancia = solve(n, arestas)
    print(*(valor if valor != float("inf") else -1 for valor in distancia))


if __name__ == '__main__':
    main()
