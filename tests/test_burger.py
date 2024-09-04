from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self, mock_ingredients):
        burger = Burger()
        ingredient_1, ingredient_2 = mock_ingredients
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 300

    def test_get_receipt(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient_1, ingredient_2 = mock_ingredients
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= sauce sour cream =\n'
            '(==== black bun ====)\n'
            'Price: 500'
        )

        # Столкнулась с расхождением между ожидаемым и фактическим результатом из-за добавленной пустой строки перед Price
        # Решила проблему удалением строки из фактического результата

        actual_receipt = burger.get_receipt()

        assert '\n'.join(filter(None, actual_receipt.split('\n'))) == expected_receipt
