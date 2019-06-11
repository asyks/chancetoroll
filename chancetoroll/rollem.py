from itertools import combinations

from typing import Tuple


NumSet = Tuple[int]
Combinations = Tuple[Tuple[int, ...]]


def successful(S: NumSet, target: int, outcome: tuple) -> bool:
    """ If any roll >= target return True """
    return any([j in outcome for j in S[S.index(target):]])


def calc_success_probability(size: int, k: int, target: int) -> float:
    """
    Calculate the probability of rolling >= <target> on <numdice> of type <size>

    First, determine the number of possible outcomes given an iterable of sides, and
    the number of dice. Next, determine the number of success outcomes given an
    iterable of sides, the number of dice, and the target value.
    """
    S: NumSet = tuple(range(1, size + 1))

    total_combinations: Combinations = tuple(combinations(S, k))

    total: float = float(len([True for outcome in total_combinations]))
    success_combinations: float = float(len(
        [True for outcome in total_combinations if successful(S, target, outcome)]
    ))

    # Prob. of Success = Successful Combs. / Total Combs.
    probability: float = success_combinations / total

    return probability
