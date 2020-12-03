from aoc.solutions.day1.part1 import run


def test_run():
    numbers = [1721, 979, 366, 299, 675, 1456]
    assert run(numbers) == 514579
