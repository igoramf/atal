def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    meio = len(nums) // 2
    esquerda = merge_sort(nums[:meio])
    direita = merge_sort(nums[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(*merge_sort(nums))


if __name__ == "__main__":
    main()
