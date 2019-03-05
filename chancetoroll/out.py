

def print_success_prob(
    typedice: int, numdice: int, targetside: int, probability: float
) -> None:
    print(
        f"Rolling {numdice}d{typedice}, probability of "
        f"beating a {targetside} is {probability:.4f}"
    )
