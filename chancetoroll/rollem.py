from __future__ import print_function

from itertools import combinations


def roll_success(N, i, rolls):
    # If any rolls >= i return True
    return any(
        [j in rolls for j in N[N.index(i):]]
    )


def success_combinations(N, k, i):
    combs = combinations(N, k)

    return len(
        [roll for roll in combs if roll_success(N, i, roll)]
    )


def total_combinations(N, k):
    combs = combinations(N, k)

    return len([roll for roll in combs])


def calc_success_probability(typedice, numdice, targetside):
    N = range(1, typedice + 1)

    a = success_combinations(N, numdice, targetside)
    b = total_combinations(N, numdice)

    # Prob. of Success = Successful Combs. / Total Combs.
    probability = float(a)/b

    return probability


def print_success_prob(typedice, numdice, targetside):
    probability = calc_success_probability(typedice, numdice, targetside)

    print(
        'Rolling {}d{}, probability of beating a {} = {}'.format(
            numdice,
            typedice,
            targetside,
            probability,
        )
    )