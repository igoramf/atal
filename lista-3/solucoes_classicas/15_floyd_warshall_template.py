def floyd_warshall(dist):
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    INF = 10**18
    n, m = map(int, input().split())
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        a, b, w = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = min(dist[a][b], w)

    floyd_warshall(dist)

    for row in dist:
        print(*[-1 if value == INF else value for value in row])


if __name__ == "__main__":
    main()
