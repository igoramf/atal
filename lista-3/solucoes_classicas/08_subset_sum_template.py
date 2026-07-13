def existe_soma(nums, alvo):
    dp = [False] * (alvo + 1)
    dp[0] = True

    for num in nums:
        for soma in range(alvo, num - 1, -1):
            dp[soma] = dp[soma] or dp[soma - num]

    return dp[alvo]


def conta_subconjuntos(nums, alvo):
    dp = [0] * (alvo + 1)
    dp[0] = 1

    for num in nums:
        for soma in range(alvo, num - 1, -1):
            dp[soma] += dp[soma - num]

    return dp[alvo]


def main():
    n, alvo = map(int, input().split())
    nums = list(map(int, input().split()))

    print("SIM" if existe_soma(nums, alvo) else "NAO")
    print(conta_subconjuntos(nums, alvo))


if __name__ == "__main__":
    main()
