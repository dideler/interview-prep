from collections import Counter
from collections import defaultdict

def is_anagram(a, b, threshold=1000000):
    """Returns true if one sequence is a permutation of the other.

    Ignores whitespace and character case.
    Compares sorted sequences if the length is below the threshold,
    otherwise compares dictionaries that contain the frequency of the
    elements.
    """
    a, b = a.strip().lower(), b.strip().lower()
    length_a, length_b = len(a), len(b)
    if length_a != length_b:
        return False
    if length_a < threshold:
        return sorted(a) == sorted(b)  # O(n log n)
    return Counter(a) == Counter(b)  # O(n)

# Or instead of using Counter() and creating two dictionaries for counting,
# you can use a single dictionary by adding and subtracting count.
def is_permutation_v1(a, b):
    d = {}
    for e in a:
        if e not in d:
            d[e] = 0
        d[e] += 1
    for e in b:
        if e not in d:
            d[e] = 0
        d[e] -= 1
    return not any(d.values())  # any() returns True if bool(element) is true for any element. bool(0) -> false.

# Even less lines of code, if we use a default dict.
def is_permutation_v2(a, b):
    d = defaultdict(int)  # Set default value to default int value, 0. Use `lambda: 1` for other values.
    for e in a:
        d[e] += 1
    for e in b:
        d[e] -= 1
    return not any(d.values())
