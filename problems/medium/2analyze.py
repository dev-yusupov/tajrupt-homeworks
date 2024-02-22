def count_words(strings):
    word_count = {}
    for string in strings:
        words = string.split()
        for word in words:
            word = word.strip('.,?!;:"')
            word = word.lower()

            word_count[word] = word_count.get(word, 0) + 1

    return word_count

strings = [
        "This is a sample string.",
        "Another sample string, a bit different from the first one.",
        "Yet another string."
    ]

print(count_words(strings=strings))