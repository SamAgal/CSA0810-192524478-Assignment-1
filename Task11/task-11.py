"""Task 11: Recommend and Defend the Final Design (External Rate Card + Decimal)."""

import os
from decimal import Decimal, ROUND_HALF_EVEN

def load_rate_card(path):
    card = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            k, v = line.split("=")
            card[k.strip()] = Decimal(v.strip())
    return card

def compute_payout(litres_str, fat_str, snf_str, card):
    litres = Decimal(litres_str)
    fat = Decimal(fat_str)
    snf = Decimal(snf_str)
    fat_steps = ((fat - card["standard_fat"]) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
    snf_steps = ((snf - card["standard_snf"]) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
    rate = card["base_rate"] + fat_steps * card["fat_step_value"] + snf_steps * card["snf_step_value"]
    return (litres * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    card = load_rate_card(input_path)
    print("Loaded Rate Card:", card)
    print("Sample Payout (10.5 L, 4.1% Fat, 8.6% SNF): Rs", compute_payout("10.5", "4.1", "8.6", card))
