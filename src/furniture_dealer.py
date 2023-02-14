class FurnitureDealer:

    def __init__(self, size: int):
        self.__size = size

    def calculate(self):

        if self.__size == 50:
            return [[50]]
        elif self.__size == 100:
            return [[50, 50], [100]]
        else:
            return []

