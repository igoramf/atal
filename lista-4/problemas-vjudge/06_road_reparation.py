import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    arestas = []

    for _ in range(m):
        a, b, custo = map(int, input().split())
        arestas.append((custo, a - 1, b - 1))

    arestas.sort()
    pai = list(range(n))
    tamanho = [1] * n

    def encontrar(vertice):
        while vertice != pai[vertice]:
            pai[vertice] = pai[pai[vertice]]
            vertice = pai[vertice]
        return vertice

    custo_total = 0
    usadas = 0

    for custo, a, b in arestas:
        raiz_a = encontrar(a)
        raiz_b = encontrar(b)

        if raiz_a == raiz_b:
            continue

        if tamanho[raiz_a] < tamanho[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a

        pai[raiz_b] = raiz_a
        tamanho[raiz_a] += tamanho[raiz_b]
        custo_total += custo
        usadas += 1

        if usadas == n - 1:
            break

    print(custo_total if usadas == n - 1 else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
