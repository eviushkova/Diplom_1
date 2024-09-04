import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        actual_name = bun.get_name()
        assert actual_name == name

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        actual_price = bun.get_price()
        assert actual_price == price
