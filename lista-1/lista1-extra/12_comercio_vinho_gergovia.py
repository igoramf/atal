def solve(casas):
    saldo = 0
    custo = 0

    for vinho in casas:
        saldo += vinho
        custo += abs(saldo)

    return custo


def main():
    while True:
        n = int(input())

        if n == 0:
            break

        casas = list(map(int, input().split()))
        result = solve(casas)

        print(result)

if __name__ == "__main__":
    main()
