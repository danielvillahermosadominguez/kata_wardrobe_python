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
            (3, []),
            (56, [[50]]),
            (78, [[50], [75]]),
            (120, [[50, 50], [75], [100], [120]])
        ],
    )
    def test_return_list_of_sizes(
            self,
            wardrobe_size,
            expected_result,
            ):

        # Given
        ikea = FurnitureDealer(wardrobe_size)

        # When
        calculated_result = ikea.calculate()

        # Then
        assert calculated_result == expected_result
