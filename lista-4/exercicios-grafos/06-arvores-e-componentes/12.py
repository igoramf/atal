import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    grafo = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b, tipo = map(int, input().split())
        a -= 1
        b -= 1
        grafo[a].append((b, tipo))
        grafo[b].append((a, tipo))

    pai = [-1] * n
    tipo_do_pai = [0] * n
    ordem = [0]

    for vertice in ordem:
        for vizinho, tipo in grafo[vertice]:
            if vizinho == pai[vertice]:
                continue
            pai[vizinho] = vertice
            tipo_do_pai[vizinho] = tipo
            ordem.append(vizinho)

    possui_escolhido = [False] * n
    resposta = []

    for vertice in reversed(ordem[1:]):
        if tipo_do_pai[vertice] == 2 and not possui_escolhido[vertice]:
            resposta.append(vertice + 1)
            possui_escolhido[vertice] = True

        possui_escolhido[pai[vertice]] |= possui_escolhido[vertice]

    print(len(resposta))
    print(*resposta)


if __name__ == "__main__":
    main()
