"""Task 3: Choose Variables and Name the Constants."""

import os

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    farmer_ref = int(lines[0])
    print(f"farmer_ref = {farmer_ref} ({type(farmer_ref).__name__})")
    farmer_ref = lines[1]
    print(f"farmer_ref = {farmer_ref} ({type(farmer_ref).__name__})")

    morning_litres, evening_litres = map(float, lines[2].split(","))
    morning_litres, evening_litres = evening_litres, morning_litres
    print(f"Swapped -> Morning: {morning_litres} L, Evening: {evening_litres} L")
