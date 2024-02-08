def count_down(i: int):
    if i == 1:
        print(1)
        return
    print(i)

    return count_down(i - 1)


def pot(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    return x * pot(x, y - 1)


# print(pot(5, 5)) 5^5 berechnen


def fibonacci(n):
    if n <= 0:
        return "Eingabe muss größer als 0 sein"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Gibt die 10. Fibonacci-Zahl aus
