from itertools import combinations

from typing import Tuple


NumSet = Tuple[int]
Combinations = Tuple[Tuple[int]]


def probability_of_success(size: int, k: int, target: int) -> float:
    """
    Calculate the probability of rolling >= <target> on <k> of type <size>

    Determine the number of total possible outcomes, and successful outcomes given an
    iterable of sides, and the number of dice. Then, calculate the success probability
    as successful outcomes/total outcomes.

    :param size: the number of sides of the dice being tested
    :param k: the number of dice being tested
    :param target: the threshold for successful outcomes
    """
    S: range = range(1, size + 1)  # dice sides being tested, e.g. d6 = (1,2,3,4,5,6)

    total_combinations: Combinations = tuple(combinations(S, k))

    total: float = 0
    successes: float = 0
    for combination in total_combinations:
        if any((True for outcome in combination if outcome >= target)):
            successes += 1
        total += 1

    return successes / total
