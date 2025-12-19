from pathlib import Path
from typing import List

from algorithms import (
    linear_search,
    binary_search,
    merge_sort,
    evaluate_password,
    generate_password,
    PasswordStats,
)

DATA_PATH = Path("data") / "weak_passwords.txt"


def load_weak_passwords(path: Path) -> List[str]:
    passwords: List[str] = []
    if not path.exists():
        print(f"Warning: {path} does not exist. Weak list will be empty.")
        return passwords
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            pw = line.strip()
            if pw:
                passwords.append(pw)
    return passwords

def main() -> None:
    weak_passwords = load_weak_passwords(DATA_PATH)
    sorted_weak = merge_sort(weak_passwords)

    while True:
        print("\n=== CSCI 377 Password Project ===")
        print("1. Check a password")
        print("2. Generate a random password")
        print("0. Quit")

        choice = input("Choice: ").strip()

        if choice == "1":
            print("Give password (empty line to go back):")
            while True:
                pw = input("> ")
                if pw == "":
                    break

                stats: PasswordStats = evaluate_password(pw)
                print(f"\nLength:     {stats.length}")
                print(f"Lowercase:  {stats.lower}")
                print(f"Uppercase:  {stats.upper}")
                print(f"Digits:     {stats.digits}")
                print(f"Symbols:    {stats.symbols}")
                print(f"Score (0–5): {stats.score}")

                if weak_passwords:
                    idx_linear = linear_search(weak_passwords, pw)
                    print("[Linear search]", "FOUND" if idx_linear != -1 else "Not found")

                    idx_binary = binary_search(sorted_weak, pw)
                    print("[Binary search]", "FOUND" if idx_binary != -1 else "Not found")
                else:
                    print("(No weak-password list loaded, only showing stats.)")

        elif choice == "2":
            length_str = input("Desired length (e.g. 12): ").strip()
            try:
                length = int(length_str)
            except ValueError:
                print("Please enter an integer.")
                continue

            pw = generate_password(length)
            print(f"\nGenerated password: {pw}")

            stats = evaluate_password(pw)
            print(
                f"Score {stats.score}/5 "
                f"(len={stats.length}, lower={stats.lower}, "
                f"upper={stats.upper}, digits={stats.digits}, symbols={stats.symbols})"
            )

        elif choice == "0":
            break
        else:
            print("Unknown choice, try again.")

if __name__ == "__main__":
    main()
