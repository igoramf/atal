def solve(n, target, nums):

    count = 0

    def backtrack(idx, current_sum):
        nonlocal count

        if idx == n:
            if current_sum == target:
                count += 1
            return
        
        backtrack(idx + 1, current_sum + nums[idx])
        backtrack(idx + 1, current_sum)

    backtrack(0, 0)

    return count

def solve2(n, target, nums):

    results = []
    
    def backtrack(idx, nums, path):
        if idx == len(nums):
            if sum(path) == target:
                results.append(path[:])
            return
        
        path.append(nums[idx])
        backtrack(idx + 1, nums, path)
        path.pop()

        backtrack(idx + 1, nums, path)

    backtrack(0, nums, [])
        
    return len(results)


def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(n, target, nums))


if __name__ == "__main__":
    main()
