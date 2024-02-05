import random
from datetime import datetime
import numpy as np
from faker import Faker


def guess_my_number() -> None:
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


def fakultaet(n: int) -> int:
    if n == 0:
        print("Abbruchbedingung 0")
        return 1
    else:
        print(f"{n}*fakultaet({n-1})")

        return n * fakultaet(n - 1)


def timestamp_to_date(timestamp) -> str:
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


# # Example usage
arr1 = [3, 1, 7]
arr2 = [8, 5, 2]
# print("Merged and sorted array:", merge_and_sort_arrays(arr1, arr2))


# print(timestamp_to_date(1675000000))
# guess_my_number()
# print(fakultaet(5))
def categorize_students(student_grades) -> dict:
    """
    Categorizes students into lists based on their grades.

    Parameters:
    - student_grades: A list of tuples, where each tuple contains (student_name, grade).

    Returns:
    - A dictionary where each key is a grade ('A', 'B', 'C', 'D', 'F') and the value is a list of student names who achieved that grade.
    """
    # Initialize a dictionary to hold the categorized names
    grade_categories = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    # Iterate through each tuple in the list
    for name, grade in student_grades:
        if grade in grade_categories:
            grade_categories[grade].append(name)

    return grade_categories


def create_random_students(num_students=5):
    # Initialize Faker
    fake = Faker()

    student_grades = []

    for _ in range(num_students):
        name = fake.first_name()

        grade = random.randint(1, 6)

        student_grades.append((name, grade))

    return student_grades


def compare_categorized_students(group1, group2):
    """
    Compares two groups of categorized students based on numerical grades.

    Parameters:
    - group1, group2: Two dictionaries with numerical grades as keys and lists of student names as values.

    Returns:
    - A string indicating which group performed better and the percentage difference between their average grades.
    """

    # Calculate average grade for a group
    def average_grade(group):
        total_grades = 0
        total_students = 0
        for grade, students in group.items():
            total_grades += grade * len(students)
            total_students += len(students)
        # Calculate the average if there are any students, otherwise return 0
        return total_grades / total_students if total_students > 0 else 0

    avg_grade_group1 = average_grade(group1)
    avg_grade_group2 = average_grade(group2)

    # Determine better group and calculate percentage difference
    if avg_grade_group1 == avg_grade_group2:
        return "Both groups performed equally well."
    else:
        better_group = "Group 1" if avg_grade_group1 < avg_grade_group2 else "Group 2"
        difference = (
            abs(avg_grade_group1 - avg_grade_group2)
            / max(avg_grade_group1, avg_grade_group2)
            * 100
        )
        return f"{better_group} performed better with an average grade difference of {difference:.2f}%."


group1 = create_random_students(25)
group2 = create_random_students(25)

group1 = categorize_students(group1)
group2 = categorize_students(group2)

result = compare_categorized_students(group1, group2)
print(result)
