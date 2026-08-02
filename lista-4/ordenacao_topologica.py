from collections import deque


def ordenar(n, arestas):
    grafo = [[] for _ in range(n + 1)]
    grau_entrada = [0] * (n + 1)

    for origem, destino in arestas:
        if not (1 <= origem <= n and 1 <= destino <= n):
            raise ValueError(f"aresta invalida: {origem} -> {destino}")
        grafo[origem].append(destino)
        grau_entrada[destino] += 1

    fila = deque(v for v in range(1, n + 1) if grau_entrada[v] == 0)
    ordem = []

    while fila:
        vertice = fila.popleft()
        ordem.append(vertice)

        for vizinho in grafo[vertice]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    return grafo, ordem if len(ordem) == n else None


def main():
    n, m = map(int, input().split())
    arestas = [tuple(map(int, input().split())) for _ in range(m)]
    grafo, ordem = ordenar(n, arestas)

    print("Arestas encontradas:")
    for origem in range(1, n + 1):
        for destino in grafo[origem]:
            print(f"{origem} -> {destino}")

    if ordem is None:
        print("Ordenacao topologica impossivel: o grafo possui ciclo.")
    else:
        print("Ordenacao topologica:", *ordem)


if __name__ == "__main__":
    main()
