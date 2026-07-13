def potencia(base, expoente, modulo):
    if expoente == 0:
        return 1 % modulo

    metade = potencia(base, expoente // 2, modulo)
    resposta = (metade * metade) % modulo

    if expoente % 2 == 1:
        resposta = (resposta * base) % modulo

    return resposta


def main():
    base, expoente, modulo = map(int, input().split())
    print(potencia(base, expoente, modulo))


if __name__ == "__main__":
    main()
