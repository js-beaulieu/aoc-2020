from aoc.solutions.day2.common import PasswordPolicy, run


def check_password(password: str, policy: PasswordPolicy):
    return policy[0] <= password.count(policy[2]) <= policy[1]


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as file:
        result = run(file.read().splitlines(), check_password)

        # correct result is: 500
        print(result)
