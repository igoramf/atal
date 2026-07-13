def troco_minimo(moedas, alvo):
    INF = alvo + 1
    dp = [INF] * (alvo + 1)
    dp[0] = 0

    for valor in range(1, alvo + 1):
        for moeda in moedas:
            if moeda <= valor:
                dp[valor] = min(dp[valor], dp[valor - moeda] + 1)

    if dp[alvo] == INF:
        return -1
    return dp[alvo]


def main():
    n, alvo = map(int, input().split())
    moedas = list(map(int, input().split()))
    print(troco_minimo(moedas, alvo))


if __name__ == "__main__":
    main()
