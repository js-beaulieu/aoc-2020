from typing import List

import pytest

from aoc.solutions.day1 import common, part1, part2


@pytest.fixture(scope="session")
def numbers() -> List[int]:
    return [1721, 979, 366, 299, 675, 1456]


@pytest.mark.parametrize(
    ("nums", "r_length", "total", "expected"),
    (
        ([1, 2, 8, 5], 2, 10, 16),
        ([10, 20, 2, 100], 3, 130, 20000),
        ([1, 4, 7, 8, 19], 4, 20, 224),
    ),
)
def test_combination_with_total_with_existing_solution(
    nums, r_length, total, expected
) -> None:
    assert common.product_of_combi_with_total(nums, r_length, total) == expected


def test_part1(numbers: List[int]) -> None:
    assert part1.run(numbers) == 514579


def test_part2(numbers: List[int]) -> None:
    assert part2.run(numbers) == 241861950
