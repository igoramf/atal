def majority_candidate(nums, left, right):
    if left == right:
        return nums[left]

    mid = (left + right) // 2
    cand_left = majority_candidate(nums, left, mid)
    cand_right = majority_candidate(nums, mid + 1, right)

    if cand_left == cand_right:
        return cand_left

    count_left = sum(1 for i in range(left, right + 1) if nums[i] == cand_left)
    count_right = sum(1 for i in range(left, right + 1) if nums[i] == cand_right)

    if count_left >= count_right:
        return cand_left
    return cand_right


def solve(nums):
    if not nums:
        return -1

    candidate = majority_candidate(nums, 0, len(nums) - 1)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))


if __name__ == "__main__":
    main()
