from unittest.mock import Mock
import pytest
from data import BUN_DATA, INGREDIENT_DATA


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BUN_DATA[0][0]
    mock_bun.get_price.return_value = BUN_DATA[0][1]
    return mock_bun


@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = INGREDIENT_DATA[0][1]
    mock_ingredient.get_type.return_value = INGREDIENT_DATA[0][0]
    mock_ingredient.get_price.return_value = INGREDIENT_DATA[0][2]
    return mock_ingredient


@pytest.fixture
def mock_ingredients():
    mock_ingredients = []
    for data in INGREDIENT_DATA[:2]:
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = data[0]
        mock_ingredient.get_name.return_value = data[1]
        mock_ingredient.get_price.return_value = data[2]
        mock_ingredients.append(mock_ingredient)
    return tuple(mock_ingredients)
