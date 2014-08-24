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

