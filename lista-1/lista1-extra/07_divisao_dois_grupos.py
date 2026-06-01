def solve(n, nums):
    
    def backtrack(start, nums, b1, b2, n):
        if start == len(nums) and len(b1) + len(b2) == len(nums):
            if sum(b1) == sum(b2):
                return True
            return
        
        for idx in range(start, n):

            b1.append(nums[idx])
            if backtrack(idx + 1, nums, b1, b2, n):
                return True
            b1.pop()

            b2.append(nums[idx])
            if backtrack(idx + 1, nums, b1,b2, n):
                return True
            b2.pop()

        return False
    
    r = backtrack(0, nums, [], [], n)
    return "YES" if r else "NO"



def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))


if __name__ == "__main__":
    main()
