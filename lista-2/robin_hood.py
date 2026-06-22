def solve(n, k, people):

    moedas = 0
    doou = 0

    for p in people:
        if p >= k:
            moedas += p
        elif p == 0 and moedas > 0:
            moedas -= 1
            doou += 1

    return doou

def main():
    
    n_tests = int(input())

    for _ in range(n_tests):
        n, k = map(int, input().split())
        people = map(int, input().split())

        r = solve(n, k, people)

        print(r)

if __name__ == "__main__":
    main()