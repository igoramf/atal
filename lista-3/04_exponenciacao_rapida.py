def fast_power(base, exp, mod):
    if exp == 0:
        return 1 % mod

    half = fast_power(base, exp // 2, mod)
    result = (half * half) % mod

    if exp % 2 == 1:
        result = (result * base) % mod

    return result


def main():
    a, b, m = map(int, input().split())
    print(fast_power(a, b, m))


if __name__ == "__main__":
    main()
