"""Wordle, but for realsies."""

__author__: str = "730655689"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string: str, char: str) -> bool:
    """Returns true if str contains char, returns false otherwise."""
    assert len(char) == 1
    ind: int = 0
    while ind < len(string):
        if string[ind] == char:
            return True
        ind += 1
    return False


def emojified(string_1: str, string_2: str) -> str:
    """Outputs emojis of green, yellow, or white boxes depending on whether a given charachter ina guess was correct, wrong, or in the wrong spot."""
    assert len(string_1) == len(string_2)
    emoj: str = ""
    ind: int = 0
    while ind < len(string_1):
        if string_1[ind] == string_2[ind]:
            emoj += GREEN_BOX
        elif contains_char(string_2, string_1[ind]):
            emoj += YELLOW_BOX
        else:
            emoj += WHITE_BOX
        ind += 1
    return emoj


def input_guess(leng: int) -> str:
    """Checks that an input is the correct length."""
    guess: str = input(f"Enter a {leng} character word: ")
    while len(guess) != leng:
        guess = input(f"That wasn't {leng} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False
    secret: str = "codes"
    while turn <= 6 and not win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            win = True
            print(f"You won in {turn}/6 turns!")
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


if __name__ == "__main__":
    main()