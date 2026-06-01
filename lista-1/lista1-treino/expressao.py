def solve(a, b, c):
    return max(
        a + b + c,
        (a + b) * c,
        a * b + c,
        a * b * c,
        a + b * c,
        a * (b + c),
    )


def main():
    nums = []
    for _ in range(3):
        nums.append(input())
    a,b,c = map(int, nums)
    print(solve(a,b,c))


if __name__ == "__main__":
    main()
