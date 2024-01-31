import random
from datetime import datetime
import numpy as np


def guess_my_number():
    lowest_number = 1
    highest_number = 100

    # Generate a random number (1-100)
    random_number = random.randint(lowest_number, highest_number)

    print(f"Guess the number! Between {lowest_number} and {highest_number}.")

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
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
                break
        except ValueError:
            print("Please enter a valid integer.")


def fakultaet(n: int):
    if n == 0:
        print("Abbruchbedingung 0")
        return 1
    else:
        print(f"{n}*fakultaet({n-1})")

        return n * fakultaet(n - 1)


def timestamp_to_date(timestamp):
    """
    Convert a Unix timestamp to a German date format (DD.MM.YYYY).

    Args:
    timestamp (int): Unix timestamp.

    Returns:
    str: Date in German format.
    """
    # above a docstring

    date_time = datetime.utcfromtimestamp(timestamp)

    return date_time.strftime("%d.%m.%Y")


def merge_and_sort_arrays(arr1: list, arr2: list) -> list:
    """
    Merge two unsorted arrays and sort the resulting array.

    Parameters:
    arr1 (numpy.ndarray): The first array.
    arr2 (numpy.ndarray): The second array.

    Returns:
    numpy.ndarray: A sorted array containing all elements from arr1 and arr2.
    """
    # Concatenate the two arrays
    merged_array = np.concatenate((arr1, arr2))
    # Sort the merged array
    sorted_array = np.sort(merged_array)

    return sorted_array


# Example usage
arr1 = [3, 1, 7]
arr2 = [8, 5, 2]
print("Merged and sorted array:", merge_and_sort_arrays(arr1, arr2))

# if __name__ == "__main__":
# print(timestamp_to_date(1675000000))
# guess_my_number()
# print(fakultaet(5))
