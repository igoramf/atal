def main():
    n = int(input())
    matriz = []

    for _ in range(n):
        ini, fim = map(int, input().split())
        matriz.append([ini, fim])

    matriz.sort(key=lambda atividade: atividade[1])

    count = 0
    ultimo_fim = -1
    for ativ in matriz:
        if ativ[0] >= ultimo_fim:
            count += 1
            ultimo_fim = ativ[1]

    return count



if __name__ == "__main__":
    r = main()
    print(r)
