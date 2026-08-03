import sys


def main():
    input = sys.stdin.buffer.readline
    n, m, q = map(int, input().split())
    infinito = 10**18
    distancia = [[infinito] * n for _ in range(n)]

    for i in range(n):
        distancia[i][i] = 0

    for _ in range(m):
        a, b, custo = map(int, input().split())
        a -= 1
        b -= 1
        if custo < distancia[a][b]:
            distancia[a][b] = custo
            distancia[b][a] = custo

    for k in range(n):
        linha_k = distancia[k]
        for i in range(n):
            ate_k = distancia[i][k]
            if ate_k == infinito:
                continue
            linha_i = distancia[i]
            for j in range(n):
                novo_custo = ate_k + linha_k[j]
                if novo_custo < linha_i[j]:
                    linha_i[j] = novo_custo

    respostas = []
    for _ in range(q):
        a, b = map(int, input().split())
        valor = distancia[a - 1][b - 1]
        respostas.append(str(valor if valor != infinito else -1))

    print("\n".join(respostas))


if __name__ == "__main__":
    main()
