import heapq
import sys


def dijkstra(grafo, inicio):
    distancia = [float("inf")] * len(grafo)
    distancia[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice = heapq.heappop(fila)
        if distancia_atual != distancia[vertice]:
            continue

        for vizinho, custo in grafo[vertice]:
            nova_distancia = distancia_atual + custo
            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancia


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]
    reverso = [[] for _ in range(n)]
    arestas = []

    for _ in range(m):
        a, b, custo = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append((b, custo))
        reverso[b].append((a, custo))
        arestas.append((a, b, custo))

    desde_inicio = dijkstra(grafo, 0)
    ate_destino = dijkstra(reverso, n - 1)
    resposta = min(
        desde_inicio[a] + custo // 2 + ate_destino[b]
        for a, b, custo in arestas
    )
    print(resposta)


if __name__ == "__main__":
    main()
