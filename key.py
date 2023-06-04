import random
from typing import List


class Key:
    def __init__(
        self,
        number_min: int,
        number_max: int,
        star_min: int,
        star_max: int,
        amount_numbers: int,
        amount_stars: int,
    ) -> None:
        self.number_min = number_min
        self.number_max = number_max
        self.star_min = star_min
        self.star_max = star_max

        self.amount_numbers = amount_numbers
        self.amount_stars = amount_stars

        self.key = []

    # generate returns a new random key for the given amount of numbers and stars
    def generate(self) -> None:
        numbers: List[int] = []
        stars: List[int] = []

        # generate numbers
        for _ in range(self.amount_numbers):
            n = random.choice(
                [
                    i
                    for i in range(self.number_min, self.number_max + 1)
                    if i not in numbers[:]
                ]
            )
            numbers.append(n)

        # generate stars
        for _ in range(self.amount_stars):
            n = random.choice(
                [
                    i
                    for i in range(self.star_min, self.star_max + 1)
                    if i not in stars[:]
                ]
            )
            stars.append(n)

        numbers.extend(stars)
        self.key = numbers

    # get_key returns the generated key
    def get_key(self) -> List[int]:
        if len(self.key) == 0:
            self.generate()

        return self.key[:]

    # get_numbers returns the numbers from the generated key
    def get_numbers(self) -> List[int]:
        return get_numbers_from_key(
            self.get_key(), self.amount_numbers, self.amount_stars
        )

    # get_stars returns the stars from the generated key
    def get_stars(self) -> List[int]:
        return get_stars_from_key(
            self.get_key(), self.amount_numbers, self.amount_stars
        )

    # check_prize compares the current key with the other and returns true if the prize can be claimed
    def check_prize(
        self, other_key: List[int], equal_numbers: int, equal_stars: int
    ) -> bool:
        # get numbers and stars from the current key
        current_key_numbers = self.get_numbers()
        current_key_stars = self.get_stars()

        # get numbers and stars from the other key
        other_key_numbers = get_numbers_from_key(
            other_key, self.amount_numbers, self.amount_stars
        )
        other_key_stars = get_stars_from_key(
            other_key, self.amount_numbers, self.amount_stars
        )

        # validate numbers
        count_equal_numbers = 0
        for current_number in current_key_numbers:
            for other_number in other_key_numbers:
                if current_number == other_number:
                    count_equal_numbers += 1
                    break

        if count_equal_numbers != equal_numbers:
            return False

        # validate stars
        count_equal_stars = 0
        for current_star in current_key_stars:
            for other_star in other_key_stars:
                if current_star == other_star:
                    count_equal_stars += 1
                    break

        if count_equal_stars != equal_stars:
            return False

        return True


# get_numbers_from_key returns the numbers from the given key
def get_numbers_from_key(
    key: List[int], amount_numbers: int, amount_stars: int
) -> List[int]:
    if len(key) != (amount_numbers + amount_stars):
        return []

    return key[0:amount_numbers]


# get_stars_from_key returns the stars from the given key
def get_stars_from_key(
    key: List[int], amount_numbers: int, amount_stars: int
) -> List[int]:
    if len(key) != (amount_numbers + amount_stars):
        return []

    return key[-amount_stars:]
