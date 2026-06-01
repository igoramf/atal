def isValid(path, l, r, x):
    s = sum(path)
    if len(path) < 2:
        return False
    if not (s >= l and s <= r):
        return False
    if max(path) - min(path) < x:
        return False
    return True 

def solve(n, l, r, x, nums):
    results = []

    def backtrack(index, path):
        
        if index == len(nums):
            if isValid(path, l, r, x):
                results.append(path[:])
            return


        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

        backtrack(index + 1, path)

    backtrack(0, [])

    return results
    


def main():
    n, l, r, x = map(int,input().split())
    nums = list(map(int, list(input().split())))
    r = solve(n, l, r, x, nums)
    print(len(r))

if __name__ == "__main__":
    main()