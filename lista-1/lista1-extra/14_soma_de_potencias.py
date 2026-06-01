def solve(x, n):
    nums = []
    base = 1

    while base ** n <= x:
        nums.append(base)
        base += 1

    len_nums = len(nums)

    count = 0
    def backtrack(idx, soma):
        nonlocal count

        if soma == x:
            count += 1
            return

        if idx == len_nums:
            return

        if soma > x:
            return
        

        backtrack(idx + 1, soma + nums[idx]**n)
        
        backtrack(idx + 1, soma)
        

    backtrack(0,0)

    return count

def main():
    x = int(input())
    n = int(input())
    result = solve(x, n)

    print(result)


if __name__ == "__main__":
    main()
