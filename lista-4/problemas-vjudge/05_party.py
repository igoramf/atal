import sys


def main():
    dados = list(map(int, sys.stdin.buffer.read().split()))
    n = dados[0]
    gerentes = dados[1 : n + 1]
    maior_profundidade = 0

    for funcionario in range(n):
        profundidade = 1
        gerente = gerentes[funcionario]

        while gerente != -1:
            profundidade += 1
            gerente = gerentes[gerente - 1]

        maior_profundidade = max(maior_profundidade, profundidade)

    print(maior_profundidade)


if __name__ == "__main__":
    main()
