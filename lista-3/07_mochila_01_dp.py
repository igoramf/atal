def solve(items, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in items:
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)

    return dp[capacity]


def main():
    n, capacity = map(int, input().split())
    items = []

    for _ in range(n):
        weight, value = map(int, input().split())
        items.append((weight, value))

    print(solve(items, capacity))


if __name__ == "__main__":
    main()
