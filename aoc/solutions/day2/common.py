from collections import Callable
from typing import List, Tuple

PasswordPolicy = Tuple[int, int, str]


def extract_policy(policy_string: str) -> PasswordPolicy:
    nums, letter = policy_string.split(" ")
    lower, upper = nums.split("-")
    return int(lower), int(upper), letter


def run(passwords: List[str], *, validator: Callable) -> int:
    counter = 0
    for line in passwords:
        policy_data, password = line.split(": ")
        policy = extract_policy(policy_data)
        if validator(password, policy):
            counter += 1

    return counter
