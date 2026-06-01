import random


def print_rules() -> None:
    print("What is the result of the expression?")


def generate_question() -> tuple:
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, correct_answer
