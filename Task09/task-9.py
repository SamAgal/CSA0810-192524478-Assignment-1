"""Task 9: Implement and Test the Calculator."""

import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(script_dir, "..", "Task07")))
import milkrate

def validate_entry(litres, fat, snf):
    return litres > 0 and (2.0 <= fat <= 7.0) and (7.0 <= snf <= 10.5)

def run_tests():
    # 1. Boundary & standard cases
    assert milkrate.rate_per_litre(3.5, 8.5) == 30.00
    assert milkrate.rate_per_litre(2.0, 8.5) == 24.00
    assert milkrate.rate_per_litre(7.0, 8.5) == 44.00

    # 2. Normal directional cases
    assert milkrate.rate_per_litre(4.2, 8.7) == 33.40
    assert milkrate.rate_per_litre(3.1, 8.3) == 27.80

    # 3. Validation checks
    assert validate_entry(10.0, 3.5, 8.5) is True
    assert validate_entry(-2.0, 3.5, 8.5) is False
    assert validate_entry(10.0, 1.8, 8.5) is False
    assert validate_entry(10.0, 7.5, 8.5) is False

    # 4. Five-entry hand-verified total from input file
    input_path = os.path.join(script_dir, "input.txt")
    entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                l, fat, snf = map(float, line.strip().split(","))
                entries.append((l, fat, snf))

    total = round(sum(milkrate.payout(l, f, s) for l, f, s in entries), 2)
    assert total == 1266.50, f"Expected 1266.50, got {total}"
    print("All automated assertions passed successfully! Verified 5-entry total = Rs", total)

if __name__ == "__main__":
    run_tests()
