from itertools import combinations

from typing import Iterable, List, Tuple


Collection = List[int]


def roll_success(N: Collection, i: int, roll: tuple) -> bool:
    """ If any roll >= i return True """
    return any([j in roll for j in N[N.index(i):]])


def success_combinations(N: Collection, k: int, i: int) -> int:
    """
    Determine the number of success outcomes given an iterable of sides,
    the number of dice, and the target value
    """
    combs: Iterable[Tuple[int, ...]] = combinations(N, k)

    return len([roll for roll in combs if roll_success(N, i, roll)])


def total_combinations(N: Collection, k: int) -> int:
    """
    Determine the number of possible outcomes given an iterable of sides,
    and the number of dice
    """
    combs = combinations(N, k)

    return len([roll for roll in combs])


def calc_success_probability(typedice: int, numdice: int, targetside: int) -> float:
    """
    Calculate the probability of rolling >= <targetside> on <numdice> of type <typedice>
    """
    N: Collection = list(range(1, typedice + 1))

    a: int = success_combinations(N, numdice, targetside)
    b: int = total_combinations(N, numdice)

    # Prob. of Success = Successful Combs. / Total Combs.
    probability: float = float(a) / b

    return probability
