def solve(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0] * m for _ in range(n)]

    if grid[0][0] == "#":
        return 0

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                dp[i][j] = 0
                continue

            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[n - 1][m - 1]


def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(solve(grid))


if __name__ == "__main__":
    main()
