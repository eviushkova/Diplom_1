from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        actual_buns = db.available_buns()
        expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]

        for i in range(len(actual_buns)):
            actual_result = (actual_buns[i].get_name(), actual_buns[i].get_price())
            expected_result = (expected_buns[i].get_name(), expected_buns[i].get_price())

            assert actual_result == expected_result

    def test_available_ingredients(self):
        db = Database()
        actual_ingredients = db.available_ingredients()
        expected_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        for i in range(len(actual_ingredients)):
            actual_result = (actual_ingredients[i].get_type(), actual_ingredients[i].get_name(), actual_ingredients[i].get_price())
            expected_result = (expected_ingredients[i].get_type(), expected_ingredients[i].get_name(), expected_ingredients[i].get_price())

            assert actual_result == expected_result
