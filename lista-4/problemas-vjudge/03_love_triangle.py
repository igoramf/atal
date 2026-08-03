import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    gosta = [vertice - 1 for vertice in map(int, input().split())]

    existe = any(gosta[gosta[gosta[i]]] == i for i in range(n))
    print("YES" if existe else "NO")


if __name__ == "__main__":
    main()
