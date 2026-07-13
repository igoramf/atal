def busca_binaria(nums, alvo):
    esquerda = 0
    direita = len(nums) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if nums[meio] == alvo:
            return meio
        if nums[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


def primeiro_maior_ou_igual(nums, alvo):
    esquerda = 0
    direita = len(nums)

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if nums[meio] >= alvo:
            direita = meio
        else:
            esquerda = meio + 1

    return esquerda


def main():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(q):
        alvo = int(input())
        print(busca_binaria(nums, alvo))


if __name__ == "__main__":
    main()
