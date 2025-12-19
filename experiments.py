from pathlib import Path
from typing import List
import time

from algorithms import linear_search, binary_search, merge_sort

DATA_PATH = Path("data") / "weak_passwords.txt"


def load_weak_passwords(path: Path) -> List[str]:
    passwords: List[str] = []
    if not path.exists():
        print(f"Error: {path} does not exist.")
        return passwords
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            pw = line.strip()
            if pw:
                passwords.append(pw)
    return passwords


def run_timing_experiment(full_weak: List[str]) -> None:
    print("\nTiming experiment")
    print("Format: N, linear_ms, sort_ms, binary_ms")

    sizes = [1000, 5000, 10000, 20000, 30000, 50000, 100000]
    for N in sizes:
        if len(full_weak) < N:
            print(f"Skipping N={N} (only have {len(full_weak)} passwords)")
            continue

        weak = full_weak[:N]
        target = "i_Hope-This_Password-Does_Not-Exist_Here-12345"

        # Linear search
        start = time.perf_counter()
        for _ in range(1000):
            linear_search(weak, target)
        linear_ms = (time.perf_counter() - start) * 1000.0

        # Merge sort
        start = time.perf_counter()
        sorted_weak = merge_sort(weak)
        sort_ms = (time.perf_counter() - start) * 1000.0

        # Binary search
        start = time.perf_counter()
        for _ in range(1000):
            binary_search(sorted_weak, target)
        binary_ms = (time.perf_counter() - start) * 1000.0

        print(f"{N}, {linear_ms:.3f}, {sort_ms:.3f}, {binary_ms:.3f}")


def main() -> None:
    weak_passwords = load_weak_passwords(DATA_PATH)
    if not weak_passwords:
        print("No weak passwords loaded.")
        return
    run_timing_experiment(weak_passwords)


if __name__ == "__main__":
    main()
