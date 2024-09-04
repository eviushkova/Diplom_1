from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'hot sauce'
    mock_ingredient.get_type.return_value = 'sauce'
    mock_ingredient.get_price.return_value = 100
    return mock_ingredient


@pytest.fixture
def mock_ingredients():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_name.return_value = 'hot sauce'
    mock_ingredient_1.get_type.return_value = 'sauce'
    mock_ingredient_1.get_price.return_value = 100
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_name.return_value = 'sour cream'
    mock_ingredient_2.get_type.return_value = 'sauce'
    mock_ingredient_2.get_price.return_value = 200
    return mock_ingredient_1, mock_ingredient_2

