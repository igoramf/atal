def solve(s):
    results = []

    def backtrack(path, used):
        if len(s) == len(path):
            st = "".join(path)
            results.append(st)
            return
        
        for ch in s:
            if ch in used:
                continue
            used.add(ch)
            path.append(ch)
            backtrack(path, used)
            path.pop()
            used.remove(ch)

    backtrack([], set())

    return results

def main():
    s = input().strip()
    result = solve(s)

    if result is not None:
        for item in result:
            print(item)


if __name__ == "__main__":
    main()
