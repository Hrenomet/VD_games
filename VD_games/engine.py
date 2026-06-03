import sys


def run_game(game_module, game_name: str = "VD Game") -> None:
    print(f"Welcome to {game_name}!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    game_module.print_rules()

    correct_count = 0
    required = 3

    while correct_count < required:
        question, correct_answer = game_module.generate_question()

        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            sys.exit(1)

    print(f"\nCongratulations, {name}!")
