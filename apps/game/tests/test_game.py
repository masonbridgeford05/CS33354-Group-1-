import pytest
from apps.game.GameInstance import GameInstance


# TC1: Valid / Valid
def test_valid_valid():
    game = GameInstance("easy")
    game.startGame("easy", "img.jpg", "Library")

    result = game.makeGuess("Library")
    assert result in ["CORRECT", "RETRY"] 


# TC2: Valid / Invalid
def test_valid_invalid_location():
    game = GameInstance("hard")
    game.startGame("hard", "img.jpg", "Library")

    with pytest.raises(ValueError):
        game.makeGuess("Bank")


# TC3: Valid / Exception
def test_valid_exception_location():
    game = GameInstance("easy")
    game.startGame("easy", "img.jpg", "Library")

    with pytest.raises(ValueError):
        game.makeGuess("")


# TC4: Invalid / Valid
def test_invalid_difficulty():
    game = GameInstance("easy")

    with pytest.raises(ValueError):
        game.startGame("impossible", "img.jpg", "Library")


# TC7: Exception / Valid
def test_null_difficulty():
    game = GameInstance("easy")

    with pytest.raises(ValueError):
        game.startGame(None, "img.jpg", "Library")
