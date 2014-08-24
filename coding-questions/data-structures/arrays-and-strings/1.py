from timeit import timeit

def contains_unique_chars(string):
    char_set = set()
    for character in string:
        if character in char_set:
            return False
        char_set.add(character)
    return True

def is_unique(s):
    """Simpler code and more efficient than the above."""
    return len(s) == len(set(s))

def assert_equal(expected, actual):
    """Basic equality assertion. Prints PASS or FAIL."""
    result = 'FAIL'

    if expected == actual:
        result = 'PASS'

    print('{}: {} -> {}'.format(result, expected, actual))

if __name__ == "__main__":
    method_a = "contains_unique_chars"
    method_b = "is_unique"
    setup_a = "from __main__ import contains_unique_chars"
    setup_b = "from __main__ import is_unique"
    print(method_a,
          timeit(method_a + "('abc')",
          setup=setup_a))
    print(method_b,
          timeit(method_b + "('abc')",
          setup=setup_b))
    print(method_a,
          timeit(method_a + "('abcdefghijklmnopqrstuvxwyz1234567890')",
          setup=setup_a))
    print(method_b,
          timeit(method_b + "('abcdefghijklmnopqrstuvxwyz1234567890')",
          setup=setup_b))

    tests = [
                ('hello', False),
                ('Dennis', False),
                ('', True),
                ('world', True),
                ('  ', False),
                ('HAHA!', False),
                ('Hypem', True)
            ]

    for test in tests:
        assert_equal(contains_unique_chars(test[0]), test[1])
        assert_equal(is_unique(test[0]), test[1])
