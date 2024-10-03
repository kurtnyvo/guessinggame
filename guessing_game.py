import random

RANDOM_LIMIT = 500

def generate_number() -> int:
    random_number = random.randint(0, RANDOM_LIMIT)
    return random_number

def main() -> None:
    attempts = 1
    random_number = generate_number()
    number_input = int(input("\nWelcome to the guessing game! Guess the number: "))

    while random_number != number_input:
        if number_input > random_number:
            number_input = int(input("Your guess is GREATER than the actual number, try again: "))
        else:
            number_input = int(input("Your guess is LESS than the actual number, try again: "))
        attempts += 1

    print(f"You got the number which was {random_number}, it took you {attempts} attempts!\n")

if __name__ == "__main__":
    main()