def solve(n, m, grid):
    pass


def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = solve(n, m, grid)

    # Imprima a resposta aqui.


if __name__ == "__main__":
    main()
