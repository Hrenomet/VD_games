import random
import math


def print_rules() -> None:
    print("Find the greatest common divisor of given numbers.")


def generate_question() -> tuple:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer


EOF
