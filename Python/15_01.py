import re
import numpy as np
import pandas as pd

l = [1, 2, 3, 1]


# get min and max of list
def get_max():
    print(max(l))


def get_min():
    print(min(l))


def remove_duplicates():
    # remove duplicates
    new = []
    for element in l:
        if element not in new:
            new.append(element)
    l = new
    print(l)


def payment_comprehension():
    payment_list = [
        {"type": "Test", "amount": 100, "date": "yesterday"},
        {"type": "Test", "amount": 200, "date": "esterday"},
    ]
    payments = [
        payment["amount"]
        for payment in payment_list
        if payment["date"].lower() == "yesterday"
    ]
    return payments
    # print(f"sum(payments)")
    # print(len(payments))


def find_all(key: str, value: str):
    payment_list = [
        {"type": "Test", "amount": 100, "date": "2024-01-15"},
        {"type": "Test", "amount": 200, "date": "2024-01-14"},
    ]
    payments = [
        payment["amount"] for payment in payment_list if payment[key].lower() == value
    ]
    return payments
    # print(f"sum(payments)")
    # print(len(payments))


# print(find_all("date", "2024-01-14"))


def is_valid_date_format(date):
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    if date_pattern.match(date):
        return True
    else:
        return False


# print(is_valid_date_format("2024-01-14"))
a = [[1, 2], [3, 4]]
c = [[10, 100]]
l = [10, 100]
# array
# list
A = np.array(a)
C = np.array(c)
print(A.shape)
print(C.shape)
# с 1×2 * a 2x2 = 1*2 ok
# a 2x2* c 1x2 = shouldnt work
# result = np.matmul (A,C)
multy = np.matmul(C, A)
print(multy.shape)
print(multy)
# [310 420] => 10*1 + 100*3, 10*2 + 100*4 => [310,420]
dotty = np.dot(l, l)
print(dotty)
multy = np.matmul(a, a)  # [[1*1+2*3 1*2+2*4] [3*1+4*3 2*3+4*4]]
print(multy)
