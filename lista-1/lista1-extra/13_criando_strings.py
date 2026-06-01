def solve(s):
    
    s = sorted(s)
    n = len(s)

    results = []
    def backtrack(path, used):
        if len(path) == n:
            results.append("".join(path))
            return

        anterior = None
        for idx in range(n):
            if used[idx]:
                continue

            if s[idx] == anterior:
                continue

            anterior = s[idx]
            used[idx] = True
            path.append(s[idx])

            backtrack(path, used)

            path.pop()
            used[idx] = False

    backtrack([], [False for _ in range(n)])

    return results

def main():
    s = input().strip()
    result = solve(s)

    print(len(result))
    for r in result:
        print(r)


if __name__ == "__main__":
    main()
