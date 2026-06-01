def isEven(n):
    return n % 2 == 0

def solve(w):
    for x in range(1, w):
        y = w - x    
        if isEven(x) and isEven(y):
            return "YES"
    return "NO"    


def main():
    w = int(input())
    print(solve(w))

if __name__ == "__main__":
    main()