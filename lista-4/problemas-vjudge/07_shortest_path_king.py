import sys


def main():
    inicio, fim = sys.stdin.buffer.read().decode().split()
    x, y = ord(inicio[0]), int(inicio[1])
    destino_x, destino_y = ord(fim[0]), int(fim[1])
    movimentos = []

    while (x, y) != (destino_x, destino_y):
        movimento = ""

        if x < destino_x:
            x += 1
            movimento += "R"
        elif x > destino_x:
            x -= 1
            movimento += "L"

        if y < destino_y:
            y += 1
            movimento += "U"
        elif y > destino_y:
            y -= 1
            movimento += "D"

        movimentos.append(movimento)

    print(len(movimentos))
    print(*movimentos, sep="\n")


if __name__ == "__main__":
    main()
