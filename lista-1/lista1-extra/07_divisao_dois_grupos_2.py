def solve(n, nums):
    total = sum(nums)

    if total % 2 != 0:
        return "NO"

    target = total // 2

    def backtrack(idx, current_sum):
        if current_sum == target:
            return True

        if current_sum > target:
            return False

        if idx == n:
            return False

        if backtrack(idx + 1, current_sum + nums[idx]):
            return True

        if backtrack(idx + 1, current_sum):
            return True

        return False

    return "YES" if backtrack(0, 0) else "NO"


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))


if __name__ == "__main__":
    main()
