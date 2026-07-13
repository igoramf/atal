def edit_distance(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                inserir = dp[i][j - 1]
                remover = dp[i - 1][j]
                trocar = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(inserir, remover, trocar)

    return dp[n][m]


def main():
    a = input().strip()
    b = input().strip()
    print(edit_distance(a, b))


if __name__ == "__main__":
    main()
