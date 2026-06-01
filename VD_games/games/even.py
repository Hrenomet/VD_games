import random


def print_rules() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_question() -> tuple:
    number = random.randint(1, 100)
    question = str(number)

    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return question, correct_answer
