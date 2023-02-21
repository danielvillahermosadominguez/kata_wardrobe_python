class FurnitureDealer:

    def __init__(self, size: int):
        self.__size = size

    def calculate(self):
        options = [50, 75, 100]
        result = []
        for option in options:
            rest = self.__size
            result_by_option = []
            while rest >= option:
                if rest >= option:
                    rest = rest - option
                    result_by_option.append(option)

            if len(result_by_option) != 0:
                result.append(result_by_option)

        return result
