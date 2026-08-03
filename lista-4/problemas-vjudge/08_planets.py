import heapq
import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        a, b, tempo = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append((b, tempo))
        grafo[b].append((a, tempo))

    bloqueados = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        bloqueados.append(set(linha[1:]))

    infinito = float("inf")
    distancia = [infinito] * n
    distancia[0] = 0
    fila = [(0, 0)]

    while fila:
        chegada, vertice = heapq.heappop(fila)
        if chegada != distancia[vertice]:
            continue
        if vertice == n - 1:
            print(chegada)
            return

        partida = chegada
        while partida in bloqueados[vertice]:
            partida += 1

        for vizinho, tempo in grafo[vertice]:
            nova_chegada = partida + tempo
            if nova_chegada < distancia[vizinho]:
                distancia[vizinho] = nova_chegada
                heapq.heappush(fila, (nova_chegada, vizinho))

    print(-1)


if __name__ == "__main__":
    main()
