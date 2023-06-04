import logging
import os
from typing import List


class Jackpot:
    def __init__(self, file_path: str, default_amount: int) -> None:
        self.file_path = file_path
        self.default_amount = default_amount

        # make sure that the directories for that path exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    # remove_old_jackpot removes the old stored jackpot amount
    def remove_old_jackpot(self) -> None:
        amount = self.default_amount

        values = self.get_file_values()
        if len(values) > 1:
            amount = values[1]

        self.set_file_values([amount])

    # get_current_jackpot returns the current stored jackpot amount
    def get_current_jackpot(self) -> int:
        amount = self.default_amount

        values = self.get_file_values()
        if len(values) != 0:
            amount = values[0]

        return amount

    # set_new_jackpot stores the new jackpot amount
    def set_new_jackpot(self, new_amount: int) -> None:
        current_amount = self.get_current_jackpot()
        self.set_file_values([current_amount, new_amount])

    # get_file_values returns all the values stored in the jackpot file
    def get_file_values(self) -> List[int]:
        values: List[int] = []

        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line.isdigit():
                        continue

                    values.append(int(line))

        except Exception as e:
            logging.error("failed to read jackpot file: {}".format(e.__str__()))

        return values

    # set_file_values stores the given values in the jackpot file
    def set_file_values(self, values: List[int]) -> List[int]:
        try:
            with open(self.file_path, "w") as f:
                for v in values:
                    f.write(str(v) + "\n")

        except Exception as e:
            logging.error(
                "failed to write to jackpot file: {}".format(self.name, e.__str__())
            )
