"""Task 2: Explore Values and Types in the Interpreter."""

from decimal import Decimal
import os
import sys

def explore_types():
    samples = [10, 10.0, "10", True, [10, 8.5]]
    for val in samples:
        print(f"Value: {val!r:10} | Type: {type(val).__name__}")

    print("\nDivision operators:")
    print("7 / 2   =", 7 / 2)
    print("7 // 2  =", 7 // 2)
    print("7 % 2   =", 7 % 2)
    print("-7 // 2 =", -7 // 2)

    print("\nFloat precision check:")
    print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
    print("0.1 + 0.2        ->", repr(0.1 + 0.2))

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

def total_decimal_from_float(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(float(amount))
    return total

if __name__ == "__main__":
    explore_types()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        payments = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    print("\n--- Financial Summation Comparison ---")
    print("float:                          ", total_float(payments))
    print("Decimal (from str):             ", total_decimal(payments))
    print("Decimal(float(amount)) [drift]: ", total_decimal_from_float(payments))
    print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
    print(f"Memory size -> int(3340): {sys.getsizeof(3340)} B | float(33.40): {sys.getsizeof(33.40)} B | Decimal('33.40'): {sys.getsizeof(Decimal('33.40'))} B")
