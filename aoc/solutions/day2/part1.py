from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class PasswordPolicy:
    minimum: int
    maximum: int
    required_letter: str


def extract_policy(policy_string: str) -> PasswordPolicy:
    nums, letter = policy_string.split(" ")
    minimum, maximum = nums.split("-")
    return PasswordPolicy(int(minimum), int(maximum), letter)


def check_password(password: str, policy: PasswordPolicy):
    return policy.minimum <= password.count(policy.required_letter) <= policy.maximum


def run(passwords: List[str]) -> int:
    counter = 0
    for line in passwords:
        policy_data, password = line.split(": ")
        policy = extract_policy(policy_data)
        if check_password(password, policy):
            counter += 1

    return counter


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as file:
        result = run(file.read().splitlines())

        # correct result is: 500
        print(result)
