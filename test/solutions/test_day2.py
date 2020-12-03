from typing import List

import pytest

from aoc.solutions.day2 import common, part1, part2


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
        ("1-3 a", (1, 3, "a")),
        ("3-8 f", (3, 8, "f")),
        ("41-99 x", (41, 99, "x")),
        ("29-302 z", (29, 302, "z")),
    ),
)
def test_extract_policy(policy_string, expectation) -> None:
    assert common.extract_policy(policy_string) == expectation


@pytest.mark.parametrize(
    ("password", "policy", "is_valid"),
    (
        ("abcde", (1, 3, "a"), True),
        ("cdefg", (1, 3, "b"), False),
        ("ccccccccc", (2, 9, "c"), True),
    ),
)
def test_part1_check_password(
    password: str, policy: common.PasswordPolicy, is_valid: bool
) -> None:
    assert part1.check_password(password, policy) == is_valid


def test_part1(passwords: List[str]) -> None:
    assert common.run(passwords, validator=part1.check_password) == 2


@pytest.mark.parametrize(
    ("password", "policy", "is_valid"),
    (
        ("abcde", (1, 3, "a"), True),
        ("cdefg", (1, 3, "b"), False),
        ("ccccccccc", (2, 9, "c"), False),
    ),
)
def test_part2_check_password(
    password: str, policy: common.PasswordPolicy, is_valid: bool
) -> None:
    assert part2.check_password(password, policy) == is_valid


def test_part2(passwords: List[str]) -> None:
    assert common.run(passwords, validator=part2.check_password) == 1
