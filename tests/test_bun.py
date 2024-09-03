import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, expected_name", [
    ("Fluorescent bun R2-D3", "Fluorescent bun R2-D3"),
    ("Krator bun N-200i", "Krator bun N-200i")
])
def test_bun_get_name(name, expected_name):
    bun = Bun(name=name, price=1976.0)
    actual_name = bun.get_name()
    assert actual_name == expected_name, f"Expected name '{expected_name}', but got '{actual_name}'"


@pytest.mark.parametrize("price, expected_price", [
    (1976.0, 1976.0),
    (2510.0, 2510.0)
])
def test_bun_get_price(price, expected_price):
    bun = Bun(name="Test Bun", price=price)
    actual_price = bun.get_price()
    assert actual_price == expected_price, f"Expected price {expected_price}, but got {actual_price}"