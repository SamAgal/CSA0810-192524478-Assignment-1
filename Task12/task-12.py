"""Task 12: Day-4 Design Challenge (2-Decimal Analyser, Seasonal Rates & >500 L Bonus)."""

import os
from decimal import Decimal, ROUND_HALF_EVEN

SEASONAL_RATES = {
    "SUMMER": {
        "base_rate": Decimal("32.00"),
        "fat_step": Decimal("0.45"),
        "snf_step": Decimal("0.30"),
    },
    "REGULAR": {
        "base_rate": Decimal("30.00"),
        "fat_step": Decimal("0.40"),
        "snf_step": Decimal("0.30"),
    },
}

STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
STEP_SIZE = Decimal("0.10")
BONUS_THRESHOLD_LITRES = Decimal("500.00")
BONUS_PER_LITRE = Decimal("0.50")

def get_rate_card(month):
    if 4 <= month <= 6:
        return SEASONAL_RATES["SUMMER"]
    return SEASONAL_RATES["REGULAR"]

def rate_per_litre(fat, snf, month=1):
    card = get_rate_card(month)
    fat_d = Decimal(str(fat))
    snf_d = Decimal(str(snf))

    fat_steps = ((fat_d - STANDARD_FAT) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
    snf_steps = ((snf_d - STANDARD_SNF) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)

    rate = card["base_rate"] + (fat_steps * card["fat_step"]) + (snf_steps * card["snf_step"])
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

def calculate_bonus(total_litres):
    litres_d = Decimal(str(total_litres))
    if litres_d > BONUS_THRESHOLD_LITRES:
        return (litres_d * BONUS_PER_LITRE).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
    return Decimal("0.00")

def ten_day_settlement(entries, month=1):
    total_litres = Decimal("0.00")
    base_payout = Decimal("0.00")

    for litres, fat, snf in entries:
        l_d = Decimal(str(litres))
        r = rate_per_litre(fat, snf, month=month)
        total_litres += l_d
        base_payout += (l_d * r).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

    bonus = calculate_bonus(total_litres)
    grand_total = (base_payout + bonus).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
    return {
        "total_litres": total_litres,
        "base_payout": base_payout,
        "bonus": bonus,
        "grand_total": grand_total,
    }

if __name__ == "__main__":
    print("Regular Month (Jan) Rate for 4.25% Fat, 8.63% SNF:", rate_per_litre("4.25", "8.63", month=1))
    print("Summer Month  (May) Rate for 4.25% Fat, 8.63% SNF:", rate_per_litre("4.25", "8.63", month=5))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                l, fat, snf = line.strip().split(",")
                entries.append((l, fat, snf))

    print("\nTen-Day Settlement (Regular - Jan):", ten_day_settlement(entries, month=1))
    print("Ten-Day Settlement (Summer  - May):", ten_day_settlement(entries, month=5))
