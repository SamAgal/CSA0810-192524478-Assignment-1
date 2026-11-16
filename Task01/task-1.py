import os

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
MIN_FAT, MAX_FAT = 2.0, 7.0
MIN_SNF, MAX_SNF = 7.0, 10.5

def calculate_entry(farmer_id: str, litres: float, fat: float, snf: float, shift: str) -> dict:
    if litres <= 0 or not (MIN_FAT <= fat <= MAX_FAT) or not (MIN_SNF <= snf <= MAX_SNF):
        raise ValueError(f"Invalid entry for farmer {farmer_id}")
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)
    amount = round(litres * rate, 2)
    return {
        "farmer_id": farmer_id,
        "shift": shift,
        "litres": litres,
        "fat": fat,
        "snf": snf,
        "rate_per_litre": rate,
        "amount": amount,
    }

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        ten_day_total = 0.0
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fid, litres_s, fat_s, snf_s, shift = line.split(",")
            res = calculate_entry(fid, float(litres_s), float(fat_s), float(snf_s), shift)
            ten_day_total = round(ten_day_total + res["amount"], 2)
            print(res)
        print(f"Ten-Day Total: Rs {ten_day_total:.2f}")
