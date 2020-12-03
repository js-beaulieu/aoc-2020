from itertools import combinations
from typing import List


def run(numbers: List[int]) -> int:
    return next(x * y for (x, y) in combinations(numbers, 2) if x + y == 2020)


if __name__ == "__main__":
    from pathlib import Path

    with open(Path(__file__).parent / "input.txt") as file:
        result = run([int(x) for x in file.read().splitlines()])

        # correct result is: 1010884
        print(result)
