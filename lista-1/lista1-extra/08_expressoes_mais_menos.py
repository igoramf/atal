def solve(n, target, nums):
    
    count = 0

    def backtrack(idx, current_sum):
        nonlocal count
        if idx == n:
            if current_sum == target:
                count += 1
            return

        
        backtrack(idx + 1, current_sum + nums[idx])
        backtrack(idx + 1, current_sum - nums[idx])

    backtrack(0, 0)

    return count

def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(n, target, nums))


if __name__ == "__main__":
    main()
