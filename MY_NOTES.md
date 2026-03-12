# My Original Thinking 
# What are the states of a game like Hangman?
Initialization state for picking the random word and setting up
Active playing state when waiting for the user to type a letter
Win state when all letters are guessed correctly
Loss state when the user ran out of attempts

# What variables are required?
secret_word (string to store the word to guess)

guessed_letters (a set or list to remember what the user already typed)

max_attempts (integer setting the limit, like 6)

incorrect_guesses (integer counting the mistakes)

# What are the rules and invariants?
The user only loses an attempt if the guessed letter is not inside the secret word.

The game ends immediately if incorrect_guesses equals max_attempts.

The game ends immediately if all the characters in secret_word are in guessed_letters.

An invariant would be the length of the masked word displayed to the screen must always exactly match the length of the secret_word.

# What kind of bugs and edge cases should we be careful about?
Case sensitivie erros, the user types "A" but the word uses "a". We need to convert everything to uppercase or lowercase.

Invalid inputs, the user types a number, a special character, or just hits enter without typing anything.

Multiple characters, the user types the whole word or two letters at once instead of a single letter.

Repeat guesses, the user guesses a letter they already tried. They shouldn't lose a life for a simple mistake like that.

# CoPilot Suggestion
App States:
Game Status — Is the game in_progress, won, or lost?
The Secret Word — The word/phrase being guessed
Guessed Letters — Which letters the player has already tried
Wrong Guesses Count — How many incorrect guesses remain (lives/attempts left)
Revealed Letters — Which letters in the word are currently visible to the player

App Variables:
secret_word
guessed_letters
wrong_count
max_attempts
game_status

App Rules and Invariants:
    Rules (What the Player Can Do)
Guess one letter at a time — Input must be a single letter
Case-insensitive — 'A' and 'a' are the same letter
No duplicate guesses — Can't guess the same letter twice
Win condition — Guess all letters in the word before running out of attempts
Lose condition — Exhaust all attempts before completing the word
Wrong guess penalty — Incorrect letter increments wrong_count

    Invariants (Properties That Must Always Hold True)
len(guessed_letters) <= 26 — Can't guess more unique letters than exist in English
wrong_count <= max_attempts — If this breaks, end the game immediately
wrong_count >= 0 and max_attempts > 0 — Negative or zero attempts don't make sense
secret_word contains only letters — No numbers, punctuation, or spaces (or you handle them specially)
guessed_letters ⊆ (secret_word ∪ incorrect guesses) — Every guessed letter is either in the word or counted as wrong
If status == "won": all letters in secret_word ⊆ guessed_letters
If status == "lost": wrong_count == max_attempts
If status == "in_progress": wrong_count < max_attempts AND not all letters revealed

App Bugs:
    State Management Bugs
Off-by-one on attempts — Incrementing wrong_count before checking if it exceeds max_attempts, causing the player to lose with one extra wrong guess
Not clearing state between rounds — guessed_letters or wrong_count persists from the previous game
Revealing the word prematurely — Showing secret_word in error messages or debug output
Stale revealed_word display — Updating guessed_letters but not recalculating what to show the player

    Logic Bugs
Case sensitivity trap — Comparing uppercase input to lowercase secret word (or vice versa) → letter appears correct but isn't marked as guessed
Duplicate guess not prevented — Allowing the same letter twice, which can artificially increase/decrease correct guesses
Win/lose condition timing — Checking for win after losing (or losing after winning on the same turn)
Wrong guess detection reversed — Flagging a correct letter as wrong because of a logic error (e.g., if letter not in word instead of if letter in word)

    Input Validation Bugs
Accepting non-letters — Numbers or symbols slip through and crash the comparison
Empty input handling — Not checking for empty strings before accessing input[0]
Multi-character input — Accepting "AB" as a guess instead of rejecting it

    Word/Display Bugs
Repeated letters in word — Revealing only the first occurrence of 'E' in "ELEVEN" instead of all of them
Spaces or hyphens — Words like "MOTHER-IN-LAW" not handling correctly (are spaces auto-revealed? Are hyphens guessable?)
Accented characters — Words with é, ñ, etc. don't match their unaccented input
Hangman drawing not updating — Display is stuck showing the same state even though wrong_count changed

    Game Flow Bugs
Continuing after game ends — Accepting guesses after status is "won" or "lost"
Never reaching "won" state — Checking if revealed_word == secret_word but missing a case where they should be equal
Incorrect attempt counting — Recording multiple attempts for a single guess, or skipping one