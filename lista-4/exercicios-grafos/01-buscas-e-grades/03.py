import sys
from collections import deque


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    grade = [input().decode().strip() for _ in range(n)]
    direcoes = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]

    tempo_monstro = [[-1] * m for _ in range(n)]
    fila = deque()
    inicio = None

    for i in range(n):
        for j in range(m):
            if grade[i][j] == "M":
                tempo_monstro[i][j] = 0
                fila.append((i, j))
            elif grade[i][j] == "A":
                inicio = (i, j)

    while fila:
        x, y = fila.popleft()
        for dx, dy, _ in direcoes:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and grade[nx][ny] != "#"
                and tempo_monstro[nx][ny] == -1
            ):
                tempo_monstro[nx][ny] = tempo_monstro[x][y] + 1
                fila.append((nx, ny))

    tempo_jogador = [[-1] * m for _ in range(n)]
    movimento_anterior = [[None] * m for _ in range(n)]
    fila = deque([inicio])
    tempo_jogador[inicio[0]][inicio[1]] = 0
    fim = None

    while fila:
        x, y = fila.popleft()
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            fim = (x, y)
            break

        for dx, dy, movimento in direcoes:
            nx, ny = x + dx, y + dy
            proximo_tempo = tempo_jogador[x][y] + 1

            if (
                0 <= nx < n
                and 0 <= ny < m
                and grade[nx][ny] != "#"
                and tempo_jogador[nx][ny] == -1
                and (
                    tempo_monstro[nx][ny] == -1
                    or proximo_tempo < tempo_monstro[nx][ny]
                )
            ):
                tempo_jogador[nx][ny] = proximo_tempo
                movimento_anterior[nx][ny] = movimento
                fila.append((nx, ny))

    if fim is None:
        print("NO")
        return

    caminho = []
    x, y = fim
    voltar = {"D": (-1, 0), "U": (1, 0), "R": (0, -1), "L": (0, 1)}

    while (x, y) != inicio:
        movimento = movimento_anterior[x][y]
        caminho.append(movimento)
        dx, dy = voltar[movimento]
        x += dx
        y += dy

    caminho.reverse()
    print("YES")
    print(len(caminho))
    print("".join(caminho))


if __name__ == "__main__":
    main()
