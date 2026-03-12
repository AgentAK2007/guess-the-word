from main import update_game_state

# --- Happy path ---
def test_correct_guess_adds_letter_and_keeps_lives():
    letters, lives = update_game_state("python", [], "p", 6)
    assert letters == ["P"]
    assert lives == 6

# Wrong guess
def test_wrong_guess_decreases_lives():
    letters, lives = update_game_state("python", [], "z", 6)
    assert letters == ["Z"]
    assert lives == 5

#Duplicate guess
def test_duplicate_guess_keeps_state():
    letters, lives = update_game_state("python", ["P"], "p", 6)
    assert letters == ["P"]
    assert lives == 6

# Invalid input (empty string, digit, and multi-char)
def test_invalid_input_empty_string():
    letters, lives = update_game_state("python", [], "", 6)
    assert letters == []
    assert lives == 6

def test_invalid_input_digit():
    letters, lives = update_game_state("python", [], "3", 6)
    assert letters == []
    assert lives == 6

def test_invalid_input_multiple_chars():
    letters, lives = update_game_state("python", [], "ab", 6)
    assert letters == []
    assert lives == 6

# Lives boundary
def test_lives_boundary_reaches_zero():
    letters, lives = update_game_state("python", [], "z", 1)
    assert letters == ["Z"]
    assert lives == 0

def test_lives_boundary_does_not_go_below_zero():
    letters, lives = update_game_state("python", ["Z"], "x", 0)
    assert letters == ["Z", "X"]
    assert lives == 0

# Case insensitivity
def test_case_insensitivity_uppercase_guess():
    letters, lives = update_game_state("python", [], "P", 6)
    assert letters == ["P"]
    assert lives == 6