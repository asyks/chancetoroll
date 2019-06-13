#!/usr/bin/env python

import argparse

from calc import calc_success_probability
from utils import parse_dstr, print_success_prob


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=(
            "Determine the probability of rolling "
            "x or greater on n individual dice."
        )
    )
    parser.add_argument(
        "dice",
        type=str,
        help=(
            "The number and type of dice to roll "
            "(e.g. 3d6 is three six-sided dice, 1d20 is one twenty-sided dice)"
        )
    )
    parser.add_argument(
        "targetside",
        type=int,
        help=(
            "The value a single dice must beat to be a success "
            "(e.g. 5 = rolls of 5 or higher are a success)"
        )
    )

    args = parser.parse_args()

    num_dice: int
    dice_type: int

    num_dice, dice_type = parse_dstr(args.dice)
    probability: float = calc_success_probability(dice_type, num_dice, args.targetside)

    print_success_prob(dice_type, num_dice, args.targetside, probability)


if __name__ == "__main__":
    main()
