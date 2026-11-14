"""Task 7: Secondary script importing milkrate module."""

import os
import milkrate as mr

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                l, fat, snf = map(float, line.strip().split(","))
                pay = mr.payout(l, fat, snf)
                print(f"Imported calculation for {l} L ({fat}% Fat, {snf}% SNF): Rs {pay:.2f}")
