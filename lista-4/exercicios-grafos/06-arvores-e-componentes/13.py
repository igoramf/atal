import sys


def componente(grade, inicio):
    n = len(grade)
    visitado = {inicio}
    pilha = [inicio]

    while pilha:
        x, y = pilha.pop()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= nx < n
                and 0 <= ny < n
                and grade[nx][ny] == "0"
                and (nx, ny) not in visitado
            ):
                visitado.add((nx, ny))
                pilha.append((nx, ny))

    return visitado


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    grade = [input().decode().strip() for _ in range(n)]

    primeiro = componente(grade, (r1 - 1, c1 - 1))
    segundo = componente(grade, (r2 - 1, c2 - 1))
    resposta = min(
        (x1 - x2) ** 2 + (y1 - y2) ** 2
        for x1, y1 in primeiro
        for x2, y2 in segundo
    )
    print(resposta)


if __name__ == "__main__":
    main()
