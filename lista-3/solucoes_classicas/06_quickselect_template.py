def particiona(nums, esquerda, direita):
    pivo = nums[direita]
    i = esquerda

    for j in range(esquerda, direita):
        if nums[j] <= pivo:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[direita] = nums[direita], nums[i]
    return i


def quickselect(nums, k):
    esquerda = 0
    direita = len(nums) - 1

    while esquerda <= direita:
        pos = particiona(nums, esquerda, direita)

        if pos == k:
            return nums[pos]
        if pos < k:
            esquerda = pos + 1
        else:
            direita = pos - 1

    return -1


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(quickselect(nums, k))


if __name__ == "__main__":
    main()
