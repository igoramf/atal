def ordenar_e_contar(nums):
    if len(nums) <= 1:
        return nums, 0

    meio = len(nums) // 2
    esquerda, inv_esq = ordenar_e_contar(nums[:meio])
    direita, inv_dir = ordenar_e_contar(nums[meio:])

    resultado = []
    i = 0
    j = 0
    inversoes = inv_esq + inv_dir

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            inversoes += len(esquerda) - i
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado, inversoes


def contar_inversoes(nums):
    _, inversoes = ordenar_e_contar(nums)
    return inversoes


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(contar_inversoes(nums))


if __name__ == "__main__":
    main()
