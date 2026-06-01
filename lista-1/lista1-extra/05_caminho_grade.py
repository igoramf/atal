def solve(n, m, grid):
    results = []
    
    def backtrack(i, j, path):
        if i >= n or j >= m:
            return

        if grid[i][j] == "#":
            return

        path.append(grid[i][j])

        if i == n - 1 and j == m - 1:
            results.append(path[:])
            path.pop()
            return

        backtrack(i, j + 1, path)
        backtrack(i + 1, j, path)

        path.pop()

    backtrack(0,0, [])
    
    return len(results)

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()
