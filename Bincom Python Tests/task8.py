# QUE: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random


def generate_and_convert():
    binary = ''.join(str(random.randint(0, 1)) for _ in range(4))
    decimal = int(binary, 2)
    # print(decimal)
    return binary, decimal


binary, decimal = generate_and_convert()
print(f"Generated binary: {binary}, Decimal equivalent: {decimal}")
