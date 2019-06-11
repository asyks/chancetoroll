from itertools import combinations

from typing import Tuple


NumSet = Tuple[int]
Combinations = Tuple[Tuple[int]]


def successful(S: NumSet, target: int, outcome: tuple) -> bool:
    """
    If any roll >= target return True

    param: S, the set of dice sides being tested, e.g. d6 = (1,2,3,4,5,6)
    param: target, the threshold for successful outcomes
    param: outcome, the selection to test for success
    """
    return any([j in outcome for j in S[S.index(target):]])


def calc_success_probability(size: int, k: int, target: int) -> float:
    """
    Calculate the probability of rolling >= <target> on <k> of type <size>

    Determine the number of total possible outcomes, and successful outcomes given an
    iterable of sides, and the number of dice. Then, calculate the success probability
    as successful outcomes/total outcomes.

    param: size, the number of sides of the dice being tested
    param: k, the number of dice being tested
    param: target, the threshold for successful outcomes
    """
    S: NumSet = tuple(range(1, size + 1))

    total_combinations: Combinations = tuple(combinations(S, k))

    total: float = float(len([True for outcome in total_combinations]))
    success_combinations: float = float(len(
        [True for outcome in total_combinations if successful(S, target, outcome)]
    ))

    return success_combinations / total
