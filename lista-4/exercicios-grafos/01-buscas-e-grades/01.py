from collections import deque

def main():
    n, m = map(int, input().split())
    grade = [input().strip() for _ in range(n)]
    if any(len(linha) != m for linha in grade):

        raise ValueError("A grade nao possui as dimensoes informadas.")

    def contar_salas():
        salas = 0
        visitado = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):

                if grade[i][j] == "." and not visitado[i][j]:
                    salas += 1

                    fila = deque([(i, j)])
                    visitado[i][j] = True

                    while fila:
                        x, y = fila.popleft()

                        for dx, dy in [(1 ,0), (-1, 0), (0, 1), (0, -1)]:
                            nx = x + dx    
                            ny = y + dy

                            dentro_da_grade = 0 <= nx < n and 0 <= ny < m                    

                            if (
                                dentro_da_grade
                                and grade[nx][ny] == '.'
                                and not visitado[nx][ny]
                            ):
                                visitado[nx][ny] = True
                                fila.append((nx, ny))
        return salas

    print(contar_salas())
             
if __name__ == "__main__":
    main()
