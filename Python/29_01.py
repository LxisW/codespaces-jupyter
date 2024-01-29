from faker import Faker
import random


def faker_exercise():
    fake = Faker()
    print(fake.name())
    # List to store student information
    students = []
    # Generate fake data for 10 students
    for _ in range(10):
        student = {
            "name": fake.name(),
            "age": random.randint(18, 25),
            "major": random.choice(["Computer Science", "Mathematics", "Physics"]),
            "gpa": round(random.uniform(2.0, 4.0), 2),
            "is_international": random.choice([True, False]),
        }
        students.append(student)
        full_name = student["name"]
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        print(first_name, last_name)

    first_names = [student["name"].split()[0] for student in students]
    print(first_names)
    print(set(first_names))
    duplicates = {
        name: first_names.count(name)
        for name in set(first_names)
        if first_names.count(name) > 1
    }
    print(duplicates)


# Fibonacci
def fibonacci_result(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci_result(n - 1) + fibonacci_result(n - 2)


# Fakultät
def factorial(n):
    # Basisfall
    if n == 0:
        return 1
    # Rekursiver Fall
    else:
        return n * factorial(n - 1)


# print(factorial(4))

# n = int(input("Enter a number: "))
# n = 5
# result = fibonacci_result(n)
# print(result)

defaultdict = __import__("collections").defaultdict
count = defaultdict(int)  # hash table,

solutions = {}


def fibonacci_of(n):
    print(f"fibonacci_of ({n})")
    count[n] += 1
    if n in solutions:
        return solutions[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    solution = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    solutions[n] = solution
    return solution


def fibinaccio_exercise():
    result = fibonacci_of(5)
    print(result)
    for key in count:
        print(f"fibonacci of {key} is called {count[key]} times")
    print(solutions)


# Recursive case
import nltk
