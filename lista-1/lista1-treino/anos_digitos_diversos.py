def allDistinct(s):
    return len(set(s)) == len(s)


def solve(year):
    while True:
        year += 1
        if allDistinct(str(year)):
            return year


def main():
    year = int(input())
    print(solve(year))


if __name__ == "__main__":
    main()
