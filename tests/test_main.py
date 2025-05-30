import os
from unittest.mock import MagicMock, patch
from fastapi import HTTPException

# Mock database engine before importing main
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
with patch('sqlalchemy.create_engine') as mock_create_engine:
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    from main import CocktailService, CocktailDB, CocktailBase

def test_get_all():
    """Test getting all cocktails."""
    # Setup mock session and service
    mock_session = MagicMock()
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    
    mock_cocktails = [
        CocktailDB(id=1, name='Mojito', description='A refreshing Cuban highball', 
                  ingredients='White rum, Sugar, Lime juice, Soda water, Mint',
                  instructions='Muddle mint leaves with sugar and lime juice. Add rum and top with soda water.'),
        CocktailDB(id=2, name='Old Fashioned', description='A classic cocktail with bourbon',
                  ingredients='Bourbon, Angostura bitters, Sugar cube, Orange peel',
                  instructions='Muddle sugar cube with bitters. Add bourbon and stir. Garnish with orange peel.')
    ]
    mock_query.all.return_value = mock_cocktails
    
    service = CocktailService(mock_session)
    result = service.get_all()
    
    assert len(result) == 2
    assert result[0].name == 'Mojito'
    assert result[1].name == 'Old Fashioned'
    mock_session.query.assert_called_once_with(CocktailDB)

def test_get_by_name():
    """Test getting a specific cocktail by name."""
    # Setup mock session and service
    mock_session = MagicMock()
    mock_query = MagicMock()
    mock_filter = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter.return_value = mock_filter
    
    mock_cocktail = CocktailDB(
        id=1, 
        name='Mojito',
        description='A refreshing Cuban highball',
        ingredients='White rum, Sugar, Lime juice, Soda water, Mint',
        instructions='Muddle mint leaves with sugar and lime juice. Add rum and top with soda water.'
    )
    mock_filter.first.return_value = mock_cocktail
    
    service = CocktailService(mock_session)
    result = service.get_by_name('Mojito')
    
    assert result.name == 'Mojito'
    mock_session.query.assert_called_once_with(CocktailDB)
    mock_query.filter.assert_called_once()

def test_get_by_name_not_found():
    """Test getting a non-existent cocktail."""
    # Setup mock session and service
    mock_session = MagicMock()
    mock_query = MagicMock()
    mock_filter = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.filter.return_value = mock_filter
    mock_filter.first.return_value = None
    
    service = CocktailService(mock_session)
    
    try:
        service.get_by_name('NonexistentCocktail')
        assert False, "Expected HTTPException"
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Cocktail 'NonexistentCocktail' not found"

def test_create_cocktail():
    """Test creating a new cocktail."""
    # Setup mock session and service
    mock_session = MagicMock()
    
    new_cocktail = CocktailBase(
        name='New Cocktail',
        description='A new cocktail',
        ingredients='Ingredient 1, Ingredient 2',
        instructions='Mix ingredients.'
    )
    
    service = CocktailService(mock_session)
    result = service.create(new_cocktail)
    
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

def test_create_duplicate_cocktail():
    """Test creating a cocktail with duplicate name."""
    # Setup mock session and service
    mock_session = MagicMock()
    mock_session.commit.side_effect = Exception("Duplicate entry")
    
    new_cocktail = CocktailBase(
        name='Existing Cocktail',
        description='A duplicate cocktail',
        ingredients='Ingredient 1, Ingredient 2',
        instructions='Mix ingredients.'
    )
    
    service = CocktailService(mock_session)
    
    try:
        service.create(new_cocktail)
        assert False, "Expected HTTPException"
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "Cocktail with name 'Existing Cocktail' already exists"
        mock_session.rollback.assert_called_once() 