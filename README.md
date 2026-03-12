# Guess The Word

Simple Hangman-style terminal game in Python.

## Requirements

- Python 3.10+
- `pytest` (for running tests)

## Run The Game

From this project folder, run:

```powershell
python main.py
```

You will be prompted to enter one letter at a time.

## Run The Tests

1. Install pytest (once):

```powershell
python -m pip install pytest
```

2. Run all tests:

```powershell
python -m pytest -q
```

3. Run only this file's tests:

```powershell
python -m pytest -q test_main.py
```

## Project Files

- `main.py`: game logic and terminal game loop
- `test_main.py`: unit tests for `update_game_state`
