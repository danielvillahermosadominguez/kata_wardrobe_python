class FurnitureDealer:

    def __init__(self, size: int):
        self.__size = size
        self.__options = [50, 75, 100, 120]

    def calculate(self):
        result = []
        for option in self.__options:
            rest = self.__size
            result_by_option = self.create_combinations(option, rest, [])

            if len(result_by_option) != 0:
                result.append(result_by_option)

        return result

    def create_combinations(self, option, rest, combinations):
        if rest >= option:
            rest = rest - option
            combinations.append(option)
            self.create_combinations(option, rest, combinations)

        return combinations
