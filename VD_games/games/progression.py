import random


def print_rules() -> None:
    print("What number is missing in the progression?")


def generate_question() -> tuple:
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(str(current_element))

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."
    question = " ".join(progression)

    return question, correct_answer
