def solve(n):
    
    results = []
    
    def backtrack(path, open_count, close_count):
        if open_count == n and close_count == n:
            results.append("".join(path))
            return

        if open_count < n:
            path.append("(")
            backtrack(path, open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(path, open_count, close_count + 1)
            path.pop()

    backtrack([], 0, 0)

    return results


def main():
    n = int(input())
    result = solve(n)

    if result is not None:
        for item in result:
            print(item)


if __name__ == "__main__":
    main()
