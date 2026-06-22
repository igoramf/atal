def main():
    dias = int(input())

    min_price = float("inf")
    custo = 0

    for _ in range(dias):
        c, p = map(int, input().split())
        min_price = min(min_price, p)
        custo += c * min_price

    print(custo)

if __name__ == "__main__":
    main()
