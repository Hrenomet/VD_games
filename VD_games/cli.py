import prompt


def welcome_user() -> None:
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def run_cli() -> None:
    print("Welcome to the VD Games!")
    welcome_user()


if __name__ == "__main__":
    run_cli()
