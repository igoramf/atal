import heapq
import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        a, b, peso = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append((b, peso))
        grafo[b].append((a, peso))

    infinito = float("inf")
    distancia = [infinito] * n
    pai = [-1] * n
    distancia[0] = 0
    fila = [(0, 0)]

    while fila:
        distancia_atual, vertice = heapq.heappop(fila)
        if distancia_atual != distancia[vertice]:
            continue

        for vizinho, peso in grafo[vertice]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                pai[vizinho] = vertice
                heapq.heappush(fila, (nova_distancia, vizinho))

    if distancia[n - 1] == infinito:
        print(-1)
        return

    caminho = []
    atual = n - 1
    while atual != -1:
        caminho.append(atual + 1)
        atual = pai[atual]

    print(*reversed(caminho))


if __name__ == "__main__":
    main()
