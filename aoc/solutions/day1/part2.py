from typing import List

from aoc.solutions.day1.common import product_of_combi_with_total


def run(numbers: List[int]) -> int:
    return product_of_combi_with_total(numbers, 3)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as file:
        result = run([int(x) for x in file.read().splitlines()])

        # correct result is: ...
        print(result)
