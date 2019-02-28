from typing import List, Tuple


def parse_dstr(dstr: str) -> Tuple[int, int]:
    """
    Parse a d notated string (e.g. 3d6, 1d20), and return a tuple of ints
    representing the number and type of dice to roll.
    """
    num: int
    dice_type: int
    parsed_dstr: List = dstr.strip().split('d')

    if len(parsed_dstr) > 2:
        raise Exception("d notated string contains not readable")

    num = int(parsed_dstr[0])
    dice_type = int(parsed_dstr[1])

    return num, dice_type
