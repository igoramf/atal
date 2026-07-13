def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(q):
        target = int(input())
        print(binary_search(nums, target))


if __name__ == "__main__":
    main()
