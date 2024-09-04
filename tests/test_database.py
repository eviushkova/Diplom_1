from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self, mock_buns_for_db):
        db = Database()
        db.buns = mock_buns_for_db
        buns = db.available_buns()

        assert buns == mock_buns_for_db

    def test_available_ingredients(self, mock_ingredients_for_db):
        db = Database()
        db.ingredients = mock_ingredients_for_db
        ingredients = db.available_ingredients()

        assert ingredients == mock_ingredients_for_db
