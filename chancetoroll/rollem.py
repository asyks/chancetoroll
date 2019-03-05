from itertools import combinations

from typing import Iterable, List, Tuple


Collection = List[int]


def roll_success(N: Collection, i: int, roll: tuple) -> bool:
    # If any roll >= i return True
    return any(
        [j in roll for j in N[N.index(i):]]
    )


def success_combinations(N: Collection, k: int, i: int) -> int:
    combs: Iterable[Tuple[int, ...]] = combinations(N, k)

    return len(
        [roll for roll in combs if roll_success(N, i, roll)]
    )


def total_combinations(N: Collection, k: int) -> int:
    combs = combinations(N, k)

    return len([roll for roll in combs])


def calc_success_probability(
    typedice: int, numdice: int, targetside: int
) -> float:
    N: Collection = list(range(1, typedice + 1))

    a: int = success_combinations(N, numdice, targetside)
    b: int = total_combinations(N, numdice)

    # Prob. of Success = Successful Combs. / Total Combs.
    probability: float = float(a)/b

    return probability
