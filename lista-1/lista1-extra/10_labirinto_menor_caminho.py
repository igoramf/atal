def find_s(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return i, j

def solve(n, m, grid):
    INF = float("inf")
    min_path = INF

    def backtrack(i, j, current_path, used):
        nonlocal min_path

        if current_path >= min_path:
            return

        if i < 0 or i >= n or j < 0 or j >= m:
            return
        
        if grid[i][j] == "#":
            return
        
        if used[i][j]:
            return
        
        used[i][j] = True
        
        if grid[i][j] == "E":
            min_path = min(current_path, min_path)
            used[i][j] = False
            return
        
        backtrack(i + 1, j, current_path + 1, used)
        backtrack(i, j + 1, current_path + 1, used)
        backtrack(i - 1, j, current_path + 1, used)
        backtrack(i, j - 1, current_path + 1, used)
        
        used[i][j] = False

    i, j = find_s(grid)
    used = [[False for _ in range(m)] for _ in range(n)]
    backtrack(i, j, 0, used)

    return min_path if min_path != INF else -1

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()
