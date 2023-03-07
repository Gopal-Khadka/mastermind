import random

COLORS = ["R", "G", "O", "B", "Y", "W"]
TRIES = 10
CODE_LEN = 5


def generate_code() -> list:
    """Generates list of random colors"""
    code = []
    for _ in range(CODE_LEN):
        color = random.choice(COLORS)
        code.append(color)
        return code


def guess_code():
    """Asks user to guess the colors."""
    is_on = True
    while is_on:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LEN:
            print(f"You must guess {CODE_LEN} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"{color} is a invalid color!!!")
                break

        else:
            break
        return guess


def check_code(guess, real_code):
    """Check user guess with generated list of colors"""
    color_counts = {}
    correct_pos, incorrect_pos = 0, 0
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[real_color] -= 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    """main game function """
    print(f"Welcome to the mastermind. You have {TRIES} attempts to guess correct.")
    code = generate_code()
    for attemps in range(TRIES):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LEN:
            print(f"You guessed code in {attemps +1} attempts.")
            break
        print(
            f"Correct positions= {correct_pos} | Incorrect positions= {incorrect_pos}"
        )
    else:
        print("You ran out of tries. The code was :", code)


is_game_on = True
while is_game_on:
    game()
    repeat = (
        input("Type Y or Yes to continue and N or No to quit the game.").lower().strip()
    )
    if repeat in ["y", "yes"]:
        game()
    else:
        is_game_on = False
