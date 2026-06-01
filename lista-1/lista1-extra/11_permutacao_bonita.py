def solve(n):
    nums = list(range(1, n + 1))

    resposta = None
    
    def backtrack(path, used):
        nonlocal resposta

        if resposta is not None:
            return

        if len(path) == n:
            resposta = path[:]
            return

        for i in range(n):
            if used[i]:
                continue 

            if path and abs(path[-1] - nums[i]) == 1:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()

            used[i] = False


    backtrack([], [False for _ in range(n)])

    return resposta

def main():
    n = int(input())
    result = solve(n)

    if result:
        print(*result)
    else:
        print("NO SOLUTION")


if __name__ == "__main__":
    main()
