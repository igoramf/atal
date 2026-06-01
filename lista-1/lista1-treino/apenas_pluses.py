def solve(a, b, c):
    maximo = 0

    def backtrack(a, b, c, ops):
        nonlocal maximo

        if ops == 0:
            calc = a * b * c
            if calc > maximo:
                maximo = calc
            return

        choices = [0, 1, 2]
        for choice in choices:
            if choice == 0:
                a += 1
            if choice == 1:
                b += 1
            if choice == 2:
                c += 1

            backtrack(a, b, c, ops - 1)

            if choice == 0:
                a -= 1
            if choice == 1:
                b -= 1
            if choice == 2:
                c -= 1

    backtrack(a, b, c, 5)
    return maximo


def main():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())
        print(solve(a, b, c))


if __name__ == "__main__":
    main()
