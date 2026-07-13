def max_crossing_sum(nums, left, mid, right):
    best_left = nums[mid]
    current = 0
    for i in range(mid, left - 1, -1):
        current += nums[i]
        best_left = max(best_left, current)

    best_right = nums[mid + 1]
    current = 0
    for i in range(mid + 1, right + 1):
        current += nums[i]
        best_right = max(best_right, current)

    return best_left + best_right


def solve_range(nums, left, right):
    if left == right:
        return nums[left]

    mid = (left + right) // 2
    best_left = solve_range(nums, left, mid)
    best_right = solve_range(nums, mid + 1, right)
    best_cross = max_crossing_sum(nums, left, mid, right)

    return max(best_left, best_right, best_cross)


def solve(nums):
    return solve_range(nums, 0, len(nums) - 1)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))


if __name__ == "__main__":
    main()
