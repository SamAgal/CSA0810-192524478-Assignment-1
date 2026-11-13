"""Task 6: Organise the Logic into Functions."""

import os

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate milk price per litre based on Fat and SNF percentage steps."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE), 2)

def payout(litres, fat, snf):
    """Calculate single-shift payout rounded to nearest paisa."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    """Aggregate total payout over a 10-day billing cycle for a list of (litres, fat, snf) tuples."""
    total = 0.0
    for litres, fat, snf in entries:
        total = round(total + payout(litres, fat, snf), 2)
    return total

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                l, fat, snf = map(float, line.strip().split(","))
                entries.append((l, fat, snf))
    print(f"Ten-day total payout: Rs {ten_day_total(entries):.2f}")
