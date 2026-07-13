def mochila_01(itens, capacidade):
    dp = [0] * (capacidade + 1)

    for peso, valor in itens:
        for c in range(capacidade, peso - 1, -1):
            dp[c] = max(dp[c], dp[c - peso] + valor)

    return dp[capacidade]


def main():
    n, capacidade = map(int, input().split())
    itens = []

    for _ in range(n):
        peso, valor = map(int, input().split())
        itens.append((peso, valor))

    print(mochila_01(itens, capacidade))


if __name__ == "__main__":
    main()
