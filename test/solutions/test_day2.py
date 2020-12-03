from typing import List

import pytest

from aoc.solutions.day2 import part1


@pytest.fixture(scope="session")
def passwords() -> List[str]:
    return [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]


@pytest.mark.parametrize(
    ("policy_string", "expectation"),
    (
        ("1-3 a", part1.PasswordPolicy(1, 3, "a")),
        ("3-8 f", part1.PasswordPolicy(3, 8, "f")),
        ("41-99 x", part1.PasswordPolicy(41, 99, "x")),
        ("29-302 z", part1.PasswordPolicy(29, 302, "z")),
    ),
)
def test_extract_policy(policy_string, expectation) -> None:
    assert part1.extract_policy(policy_string) == expectation


@pytest.mark.parametrize(
    ("password", "policy", "is_valid"),
    (
        ("abcde", part1.PasswordPolicy(1, 3, "a"), True),
        ("cdefg", part1.PasswordPolicy(1, 3, "b"), False),
        ("ccccccccc", part1.PasswordPolicy(2, 9, "c"), True),
    ),
)
def test_check_password(
    password: str, policy: part1.PasswordPolicy, is_valid: bool
) -> None:
    assert part1.check_password(password, policy) == is_valid


def test_part1(passwords: List[str]) -> None:
    assert part1.run(passwords) == 2
