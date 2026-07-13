def sort_and_count(nums):
    if len(nums) <= 1:
        return nums, 0

    mid = len(nums) // 2
    left, inv_left = sort_and_count(nums[:mid])
    right, inv_right = sort_and_count(nums[mid:])

    merged = []
    i = 0
    j = 0
    inversions = inv_left + inv_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


def solve(nums):
    _, inversions = sort_and_count(nums)
    return inversions


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))


if __name__ == "__main__":
    main()
