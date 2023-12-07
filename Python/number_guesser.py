import random


def guess_my_number():
    lowest_number = 1
    highest_number = 100

    # Generate a random number (1-100)
    random_number = random.randint(lowest_number, highest_number)

    print(
        f"Guess the number! Between {lowest_number} and {highest_number}.")

    attempts = 0

    while True:
        attempts += 1
        try:
            # player's guess
            guess = int(input("Enter your guess: "))

            # Check  guess
            if guess < random_number:
                print("Too low. Try again.")
            elif guess > random_number:
                print("Too high. Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    guess_my_number()
