def solve(coins, target):
    INF = target + 1
    dp = [INF] * (target + 1)
    dp[0] = 0

    for value in range(1, target + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    if dp[target] == INF:
        return -1
    return dp[target]


def main():
    n, target = map(int, input().split())
    coins = list(map(int, input().split()))
    print(solve(coins, target))


if __name__ == "__main__":
    main()
