from dataclasses import dataclass
import random
import string


@dataclass
class PasswordStats:
    length: int
    lower: int
    upper: int
    digits: int
    symbols: int
    score: int


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def merge_sort(arr):
    # O(n log n) divide and conquer sorting
    n = len(arr)
    if n <= 1:
        return arr[:]
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    # helper for merge_sort that will combine two sorted lists
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def binary_search(arr, target):
    # O(log n) arr needs to be sorted for this to work
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def evaluate_password(pw):
    # O(l) counts character types and calculates strength score
    lower = upper = digits = symbols = 0
    for c in pw:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isdigit():
            digits += 1
        else:
            symbols += 1
    length = len(pw)

    # score based on length and character variety
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if lower > 0 and upper > 0:
        score += 1
    if digits > 0:
        score += 1
    if symbols > 0:
        score += 1

    return PasswordStats(
        length=length,
        lower=lower,
        upper=upper,
        digits=digits,
        symbols=symbols,
        score=score,
    )


def generate_password(length):
    # O(l) generates a random password with at least one of each char type

    if length < 4:
        length = 4

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    all_chars = lowers + uppers + digits + symbols

    pw_chars = []

    # make sure we have at least one of each type
    pw_chars.append(random.choice(lowers))
    pw_chars.append(random.choice(uppers))
    pw_chars.append(random.choice(digits))
    pw_chars.append(random.choice(symbols))

    # fill the rest randomly
    while len(pw_chars) < length:
        pw_chars.append(random.choice(all_chars))

    random.shuffle(pw_chars)
    return "".join(pw_chars)
