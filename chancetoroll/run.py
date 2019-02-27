#!/usr/bin/env python

import argparse

from rollem import print_success_prob


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=(
            'Determine the probability of rolling '
            'x or greater on n individual dice.'
        )
    )
    parser.add_argument(
        'typedice',
        type=int,
        help=(
            'The type of dice to roll '
            '(4 = d4, 6 = d6, 20 = d20, etc.)'
        )
    )
    parser.add_argument(
        'numdice',
        type=int,
        help=(
            'The number of dice to roll '
            '(1 = roll 1 dice, 2 = roll 2 dice, etc.)'
        )
    )
    parser.add_argument(
        'targetside',
        type=int,
        help=(
            'The value a single dice must beat to be a success '
            '(e.g. 5 = rolls of 5 or higher are a success)'
        )
    )

    args = parser.parse_args()

    print_success_prob(
        args.typedice,
        args.numdice,
        args.targetside,
    )


if __name__ == '__main__':
    main()
