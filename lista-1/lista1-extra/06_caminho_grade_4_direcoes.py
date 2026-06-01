def find_s(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return i, j

def solve(n, m, grid):

    def backtrack(i, j, used):

        if i < 0 or i >= n or j < 0 or j >= m:
            return
        
        if grid[i][j] == "#":
            return
        
        if used[i][j]:
            return
        
        used[i][j] = True
        
        if grid[i][j] == "E":
            return True
        
        if backtrack(i + 1, j, used):
            return True
        if backtrack(i - 1, j, used):
            return True
        if backtrack(i, j + 1, used):
            return True
        if backtrack(i, j - 1, used):
            return True
        
        used[i][j] = False


    start_i, start_j = find_s(grid)
    s = backtrack(start_i, start_j, [[False for _ in range(m)] for _ in range(n)])

    return "YES" if s else "NO"

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(solve(n, m, grid))


if __name__ == "__main__":
    main()
