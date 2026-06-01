def solve(chars, k):
    
    results = []
    chars = list(chars)

    def backtrack(path):
        if len(path) == k:
            results.append("".join(path[:]))
            return

        for ch in chars:
            path.append(ch)
            backtrack(path)
            path.pop()
    
    backtrack([])

    return results
    


def main():
    chars = input().strip()
    k = int(input())
    result = solve(chars, k)

    if result is not None:
        for item in result:
            print(item)


if __name__ == "__main__":
    main()
