import pytest

from src.furniture_dealer import FurnitureDealer


class TestWardRobe:
    @pytest.mark.parametrize(
        "wardrobe_size,expected_result",
        [
            (0, []),
            (50, [[50]]),
            (75, [[50], [75]]),
            (100, [[50, 50], [75], [100]]),
        ],
    )
    def test_return_list_of_sizes(
            self,
            wardrobe_size,
            expected_result,
            ):
        #When
        ikea = FurnitureDealer(wardrobe_size)
        calculated_result = ikea.calculate()

        #Then
        assert calculated_result == expected_result
