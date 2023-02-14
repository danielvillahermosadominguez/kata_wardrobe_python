from src.furniture_dealer import FurnitureDealer


def test_return_empty_size_empty_wardrobe():
    ikea = FurnitureDealer(0)
    assert ikea.calculate() == []


def test_return_only_one_element_for_50_wardrobe():
    ikea = FurnitureDealer(50)
    assert ikea.calculate() == [[50]]

def test_return_only_one_element_for_100_wardrobe():
    ikea = FurnitureDealer(100)
    assert ikea.calculate() == [[50, 50], [100]]
