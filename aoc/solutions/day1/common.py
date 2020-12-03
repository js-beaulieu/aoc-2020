from itertools import combinations
from math import prod
from typing import List


def product_of_combi_with_total(numbers: List[int], r_length, total=2020):
    return next(
        prod(combi) for combi in combinations(numbers, r_length) if sum(combi) == total
    )
