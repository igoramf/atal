def contar_formas(moedas, alvo):
    dp = [0] * (alvo + 1)
    dp[0] = 1

    for moeda in moedas:
        for valor in range(moeda, alvo + 1):
            dp[valor] += dp[valor - moeda]

    return dp[alvo]


def main():
    n, alvo = map(int, input().split())
    moedas = list(map(int, input().split()))
    print(contar_formas(moedas, alvo))


if __name__ == "__main__":
    main()
