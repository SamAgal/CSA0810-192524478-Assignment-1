"""Task 10: Compare Expectations with Execution."""

import os
import time
from decimal import Decimal, ROUND_HALF_EVEN

def run_scale_benchmark(n_entries):
    entries = [(Decimal("11.35"), Decimal("4.1"), Decimal("8.6")) for _ in range(n_entries)]

    t0 = time.perf_counter()
    f_total = 0.0
    for l, f, s in entries:
        rate = 30.0 + round((float(f) - 3.5) / 0.1) * 0.40 + round((float(s) - 8.5) / 0.1) * 0.30
        f_total += round(float(l) * rate, 2)
    t_float = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    d_total = Decimal("0.00")
    for l, f, s in entries:
        fat_steps = ((f - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
        snf_steps = ((s - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
        rate = Decimal("30.00") + fat_steps * Decimal("0.40") + snf_steps * Decimal("0.30")
        pay = (l * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
        d_total += pay
    t_dec = (time.perf_counter() - t1) * 1000

    t2 = time.perf_counter()
    rate_cache = {}
    m_total = Decimal("0.00")
    for l, f, s in entries:
        key = (f, s)
        if key not in rate_cache:
            fat_steps = ((f - Decimal("3.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
            snf_steps = ((s - Decimal("8.5")) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
            rate_cache[key] = Decimal("30.00") + fat_steps * Decimal("0.40") + snf_steps * Decimal("0.30")
        m_total += (l * rate_cache[key]).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
    t_memo = (time.perf_counter() - t2) * 1000

    print(f"N = {n_entries:6d} | Float: {f_total:12.4f} ({t_float:6.2f} ms) | Decimal: {d_total:12} ({t_dec:6.2f} ms) | Memoized: {m_total:12} ({t_memo:6.2f} ms)")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                run_scale_benchmark(int(line.strip()))
