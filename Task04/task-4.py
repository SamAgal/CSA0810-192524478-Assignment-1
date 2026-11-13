"""Task 4: Write Correct Expressions."""

import math
import os

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def compare_step_methods(fat_val):
    raw_steps = (fat_val - 3.5) / 0.1
    r_steps = round(raw_steps)
    i_steps = int(raw_steps)
    f_steps = math.floor(raw_steps)
    print(f"Fat = {fat_val}: raw={raw_steps:.16f}")
    print(f"  round() -> steps={r_steps:2d}, rate={BASE_RATE + r_steps * FAT_STEP_VALUE:.2f}")
    print(f"  int()   -> steps={i_steps:2d}, rate={BASE_RATE + i_steps * FAT_STEP_VALUE:.2f}")
    print(f"  floor() -> steps={f_steps:2d}, rate={BASE_RATE + f_steps * FAT_STEP_VALUE:.2f}")

if __name__ == "__main__":
    print("Surprise 1: (4.2 - 3.5) / 0.1 =", repr((4.2 - 3.5) / 0.1))
    print("Surprise 2: -3 ** 2 =", -3 ** 2, "vs (-3) ** 2 =", (-3) ** 2)
    print("Surprise 3: round(2.675, 2) =", round(2.675, 2))
    print("\n--- Rate Step Comparison ---")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                compare_step_methods(float(line.strip()))
