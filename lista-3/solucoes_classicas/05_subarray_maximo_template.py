def melhor_cruzando(nums, esquerda, meio, direita):
    melhor_esq = nums[meio]
    soma = 0
    for i in range(meio, esquerda - 1, -1):
        soma += nums[i]
        melhor_esq = max(melhor_esq, soma)

    melhor_dir = nums[meio + 1]
    soma = 0
    for i in range(meio + 1, direita + 1):
        soma += nums[i]
        melhor_dir = max(melhor_dir, soma)

    return melhor_esq + melhor_dir


def resolver(nums, esquerda, direita):
    if esquerda == direita:
        return nums[esquerda]

    meio = (esquerda + direita) // 2
    melhor_esq = resolver(nums, esquerda, meio)
    melhor_dir = resolver(nums, meio + 1, direita)
    melhor_meio = melhor_cruzando(nums, esquerda, meio, direita)

    return max(melhor_esq, melhor_dir, melhor_meio)


def subarray_maximo(nums):
    return resolver(nums, 0, len(nums) - 1)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(subarray_maximo(nums))


if __name__ == "__main__":
    main()
