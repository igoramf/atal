from dataclasses import dataclass, field
from heapq import heappop, heappush


@dataclass(order=True)
class Node:
    # O heapq remove primeiro o no com menor priority.
    # Neste problema, priority sera o bound, pois queremos minimizar custo.
    priority: int
    level: int = field(compare=False)
    cost_so_far: int = field(compare=False)
    assigned_tasks: tuple[int, ...] = field(compare=False)
    bound: int = field(compare=False)


def lower_bound(matriz, level, assigned_tasks):
    # TODO: calcule o limite otimista dos trabalhadores restantes.
    # Retorne apenas a estimativa do restante, sem somar cost_so_far.
    used_tasks = set(assigned_tasks)
    estimate = 0

    for worker in range(level, len(matriz)):
        best_task_cost = min(
            matriz[worker][task]
            for task in range(len(matriz))
            if task not in used_tasks
        )
        estimate += best_task_cost

    return estimate


def solve(matriz):
    n = len(matriz)

    root_bound = lower_bound(matriz, 0, ())
    root = Node(
        priority=root_bound,
        level=0,
        cost_so_far=0,
        assigned_tasks=(),
        bound=root_bound,
    )

    best_cost = float("inf")
    best_assignment = ()

    heap = []
    heappush(heap, root)

    while heap:
        node = heappop(heap)

        # Aqui voce esta visitando o no mais promissor ate agora.
        # Ele e o mais promissor porque tem o menor bound no heap.

        # TODO: poda.
        # Se node.bound >= best_cost, esse ramo nao consegue melhorar a resposta.

        if node.bound >= best_cost:
            continue

        # TODO: caso completo.
        # Se node.level == n, todos os trabalhadores ja receberam tarefa.
        # Atualize best_cost e best_assignment se node.cost_so_far for melhor.

        if node.level == n:
            if node.cost_so_far < best_cost:
                best_cost = node.cost_so_far
                best_assignment = node.assigned_tasks
            continue

        worker = node.level
        used_tasks = set(node.assigned_tasks)

        # TODO: branch.
        # Gere os filhos tentando atribuir cada tarefa ainda nao usada
        # ao trabalhador atual.
        for task in range(n):
            if task in used_tasks:
                continue

            new_assigned = node.assigned_tasks + (task,)
            new_cost = node.cost_so_far + matriz[worker][task]
            optimistic_rest = lower_bound(matriz, worker + 1, new_assigned)
            new_bound = new_cost + optimistic_rest

            # TODO: decida se este filho merece entrar no heap.
            # Se ele ainda puder bater best_cost, empurre no heap.

            if new_bound < best_cost:
                heappush(heap, Node(
                    priority=new_bound,
                    level=worker + 1,
                    cost_so_far=new_cost,
                    assigned_tasks=new_assigned,
                    bound=new_bound,
                ))

    return best_cost, best_assignment


def main():
    n = int(input())
    matriz = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matriz.append(row)

    best_cost, _ = solve(matriz)
    print(best_cost)


if __name__ == "__main__":
    main()
