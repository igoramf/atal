from collections import deque

def main():
    n, m = map(int, input().split())
    grade = [input().strip() for _ in range(n)]
    if any(len(linha) != m for linha in grade):

        raise ValueError("A grade nao possui as dimensoes informadas.")

    def labirinto():
        inicio = None
        fim = None

        for i in range(n):
            for j in range(m):
                if grade[i][j] == "A":
                    inicio = (i, j)
                elif grade[i][j] == "B":
                    fim = (i, j)

        if inicio is None or fim is None:
            raise ValueError("A grade precisa conter A e B.")

        visitado = [[False] * m for _ in range(n)]
        pai = [[None] * m for _ in range(n)]

        fila = deque([inicio])
        visitado[inicio[0]][inicio[1]] = True
        direcoes = [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]

        while fila:
            x, y = fila.popleft()

            if (x, y) == fim:
                break

            for dx, dy, move in direcoes:
                nx = x + dx
                ny = y + dy

                can_visit = 0 <= nx < n and 0 <= ny < m
                if can_visit and grade[nx][ny] != "#" and not visitado[nx][ny]:
                    visitado[nx][ny] = True
                    pai[nx][ny] = (x, y, move)
                    fila.append((nx, ny))

        if not visitado[fim[0]][fim[1]]:
            return "NO"

        caminho = []
        atual = fim

        while atual != inicio:
            x, y, move = pai[atual[0]][atual[1]]
            caminho.append(move)
            atual = (x, y)

        caminho.reverse()
        return f"YES\n{len(caminho)}\n{''.join(caminho)}"
    print(labirinto())
             
if __name__ == "__main__":
    main()
