def solve(distance, max_range, stations):
    stations.sort()

    position = 0
    stops = 0
    index = 0

    while position + max_range < distance:
        next_position = position

        while index < len(stations) and stations[index] <= position + max_range:
            if stations[index] > position:
                next_position = stations[index]
            index += 1

        if next_position == position:
            return -1

        position = next_position
        stops += 1

    return stops


def main():
    distance, max_range, n = map(int, input().split())
    stations = list(map(int, input().split())) if n > 0 else []
    print(solve(distance, max_range, stations))


if __name__ == "__main__":
    main()
