def solve(n, k, skills):
    maximo = 0

    def backtrack(path, start):
        nonlocal maximo
        if len(path) == k:
            maximo = max(maximo, sum(path))
            return
        
        for idx in range(start, n):
            path.append(skills[idx])
            backtrack(path, idx + 1)
            path.pop()

    backtrack([], 0)

    return maximo


def main():
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    print(solve(n, k, skills))


if __name__ == "__main__":
    main()
