import random
import sys


def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    print("Welcome to the VD Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    required_correct = 3

    while correct_answers < required_correct:
        number = random.randint(1, 100)
        print(f"\nQuestion: {number}")

        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            sys.exit(1)

    print(f"\nCongratulations, {name}!")


if __name__ == "__main__":
    main()
