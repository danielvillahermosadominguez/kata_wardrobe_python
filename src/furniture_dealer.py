import numpy as np

class FurnitureDealer:

    def __init__(self, size: int):
        self.__size = size
        self.__options = [50, 75, 100, 120]

    def calculate(self):
        result = []

        for index, item in enumerate(self.__options):
            rest = self.__size
            result_by_option = []

            if rest >= self.__options[index]:
                result_by_option = self.create_combinations(index, rest, [])

            if len(result_by_option) != 0:
                result.append(result_by_option)

        return result

    #idea inicial
    def create_combinations(self, index, rest, combinations):
        option = self.__options[index]
        previousOption = self.__options[index-1]

        if rest >= option:
            rest = rest - option
            combinations.append(option)
            self.create_combinations(index, rest, combinations)
        elif rest >= previousOption:
            rest = rest - previousOption
            combinations.append(previousOption)
            self.create_combinations(index-1, rest, combinations)

        return combinations
