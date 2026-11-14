"""Task 8: Plan the Algorithm Before Coding (Executable Hand Trace Verification)."""

import os

def run_hand_trace(entries):
    ten_day_total = 0.00
    print(f"{'Step':<5} {'Litres':<8} {'Fat':<6} {'SNF':<6} {'Valid':<7} {'Rate':<8} {'Pay':<9} {'Total':<9}")
    for idx, (litres, fat, snf) in enumerate(entries, start=1):
        if litres > 0 and (2.0 <= fat <= 7.0) and (7.0 <= snf <= 10.5):
            fat_steps = round((fat - 3.5) / 0.1)
            snf_steps = round((snf - 8.5) / 0.1)
            rate = round(30.00 + fat_steps * 0.40 + snf_steps * 0.30, 2)
            entry_pay = round(litres * rate, 2)
            ten_day_total = round(ten_day_total + entry_pay, 2)
            print(f"{idx:<5} {litres:<8.1f} {fat:<6.1f} {snf:<6.1f} {'Yes':<7} {rate:<8.2f} {entry_pay:<9.2f} {ten_day_total:<9.2f}")
        else:
            print(f"{idx:<5} {litres:<8.1f} {fat:<6.1f} {snf:<6.1f} {'No':<7} {'-':<8} {'-':<9} {ten_day_total:<9.2f}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    trace_entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                l, fat, snf = map(float, line.strip().split(","))
                trace_entries.append((l, fat, snf))
    run_hand_trace(trace_entries)
