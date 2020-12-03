from operator import xor

from aoc.solutions.day2.common import PasswordPolicy, run


def check_password(password: str, policy: PasswordPolicy):
    letter = policy[2]
    return xor(
        password[policy[0] - 1] == letter,
        password[policy[1] - 1] == letter,
    )


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as file:
        result = run(file.read().splitlines(), validator=check_password)

        # correct result is: 313
        print(result)
