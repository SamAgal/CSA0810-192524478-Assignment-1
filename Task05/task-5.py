"""Task 5: Read Input and Convert Types."""

import os

def is_valid_number(text):
    cleaned = text.strip()
    if cleaned.startswith("-"):
        cleaned = cleaned[1:]
    return cleaned.replace(".", "", 1).isdigit()

def parse_entry(litres_str, fat_str, snf_str):
    if not (is_valid_number(litres_str) and is_valid_number(fat_str) and is_valid_number(snf_str)):
        raise ValueError(f"Non-numeric input detected: ({litres_str!r}, {fat_str!r}, {snf_str!r})")
    litres = float(litres_str)
    fat = float(fat_str)
    snf = float(snf_str)
    if litres <= 0:
        raise ValueError("Litres must be strictly positive.")
    if not (2.0 <= fat <= 7.0):
        raise ValueError(f"Fat {fat}% out of valid range [2.0, 7.0].")
    if not (7.0 <= snf <= 10.5):
        raise ValueError(f"SNF {snf}% out of valid range [7.0, 10.5].")
    return litres, fat, snf

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            l_s, f_s, s_s = line.split("|")
            try:
                l, f, s = parse_entry(l_s, f_s, s_s)
                amount = l * 31.50
                print(f"Valid    -> {l:6.2f} L | Fat: {f:4.1f}% | SNF: {s:4.1f}% | Amount: Rs {amount:8.2f}")
            except ValueError as err:
                print(f"Rejected -> {err}")
