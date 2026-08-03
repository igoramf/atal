import sys


def main():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    grade = [list(input().decode().strip()) for _ in range(n)]
    livres = sum(linha.count(".") for linha in grade)
    manter = livres - k
    inicio = next(
        ((i, j) for i in range(n) for j in range(m) if grade[i][j] == "."),
        None,
    )

    for i in range(n):
        for j in range(m):
            if grade[i][j] == ".":
                grade[i][j] = "X"

    if manter > 0:
        pilha = [inicio]
        grade[inicio[0]][inicio[1]] = "."
        manter -= 1

        while manter:
            x, y = pilha.pop()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < n and 0 <= ny < m and grade[nx][ny] == "X":
                    grade[nx][ny] = "."
                    pilha.append((nx, ny))
                    manter -= 1
                    if manter == 0:
                        break

    print("\n".join("".join(linha) for linha in grade))


if __name__ == "__main__":
    main()
