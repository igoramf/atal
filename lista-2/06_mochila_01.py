from dataclasses import dataclass, field
from heapq import heappop, heappush


@dataclass(order=True)
class Node:
    # Para maximizar, queremos maior bound primeiro.
    # Como heapq e min-heap, usaremos priority = -bound.
    priority: float
    level: int = field(compare=False)
    value: int = field(compare=False)
    weight: int = field(compare=False)
    taken_items: tuple[int, ...] = field(compare=False)
    bound: float = field(compare=False)

def fractional_bound(items, capacity, level, current_weight, current_value):
    if current_weight > capacity:
        return 0

    bound = float(current_value)
    total_weight = current_weight
    i = level

    while i < len(items) and total_weight + items[i][0] <= capacity:
        weight, value = items[i]
        total_weight += weight
        bound += value
        i += 1

    if i < len(items):
        weight, value = items[i]
        remaining_capacity = capacity - total_weight
        bound += remaining_capacity * (value / weight)

    return bound

def solve(matriz, capacity):

    n = len(matriz)
    items = sorted(matriz, key=lambda item: item[1] / item[0], reverse=True)

    root_bound = fractional_bound(items, capacity, 0, 0, 0)
    root = Node(
        priority=-root_bound,
        level=0,
        value=0,
        weight=0,
        taken_items=(),
        bound=root_bound
    )

    best_value = 0
    best_items = ()
    heap = []
    heappush(heap, root)

    while heap:
        node = heappop(heap)

        if node.bound <= best_value:
            continue

        if node.level == n:
            continue

        item_index = node.level
        item_weight, item_value = items[item_index]
        next_level = node.level + 1

        take_weight = node.weight + item_weight
        take_value = node.value + item_value
        take_items = node.taken_items + (item_index,)

        if take_weight <= capacity:
            if take_value > best_value:
                best_value = take_value
                best_items = take_items

            take_bound = fractional_bound(
                items,
                capacity,
                next_level,
                take_weight,
                take_value,
            )

            if take_bound > best_value:
                heappush(heap, Node(
                    priority=-take_bound,
                    level=next_level,
                    value=take_value,
                    weight=take_weight,
                    taken_items=take_items,
                    bound=take_bound,
                ))

        skip_bound = fractional_bound(
            items,
            capacity,
            next_level,
            node.weight,
            node.value,
        )

        if skip_bound > best_value:
            heappush(heap, Node(
                priority=-skip_bound,
                level=next_level,
                value=node.value,
                weight=node.weight,
                taken_items=node.taken_items,
                bound=skip_bound,
            ))

    return best_value

def main():
    n, capacity = map(int, input().split())
    matriz = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matriz.append(row)

    best = solve(matriz, capacity)
    print(best)


if __name__ == "__main__":
    main()
