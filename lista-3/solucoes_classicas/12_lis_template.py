def lis_quadratico(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(lis_quadratico(nums))


if __name__ == "__main__":
    main()
