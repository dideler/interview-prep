def contains_unique_chars(string):
    char_set = set()
    for character in string:
        if character in char_set:
            return False
        char_set.add(character)
    return True

print(contains_unique_chars('hello'))
print(contains_unique_chars('world'))
