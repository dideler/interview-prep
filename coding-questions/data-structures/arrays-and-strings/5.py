def compress(s):
    """Returns a compressed string if smaller than the original."""
    compressed = []
    count = 1
    for i, char in enumerate(s):
        if i + 1 < len(s) and char == s[i + 1]:
            count += 1
        else:
            compressed.append('{}{}'.format(char, count)) # Or append char, append count.
            count = 1
    compressed_string = ''.join(compressed)
    if len(compressed_string) < len(s):
        return compressed_string
    return s

print compress('abc')
print compress('aabbcc')
print compress('aabcccccaaa')
