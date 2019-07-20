from typing import List, Tuple


def parse_dstr(dstr: str) -> Tuple[int, int]:
    """
    Parse a d notated string (e.g. 3d6, 1d20), and return a tuple of ints
    representing the number and type of dice to roll
    """
    num: int
    dice_type: int
    parsed_dstr: List = dstr.strip().split("d")

    if len(parsed_dstr) > 2:
        raise Exception("d notated string format not unrecognized")

    num = int(parsed_dstr[0])
    dice_type = int(parsed_dstr[1])

    return num, dice_type


def print_success_prob(
    dice_type: int, num_dice: int, target: int, probability: float
) -> None:
    """
    Print the calculated success probability as a formatted string
    """
    print(
        f"Rolling {num_dice}d{dice_type}, probability of "
        f"beating a {target} is {probability:.4f}"
    )
