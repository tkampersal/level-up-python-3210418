def sort_words(words):
    print("parameter: " + words)
    print(f"split: {words.split()}")
    print(f"sorted1: {sorted(words.split())}")
    print(f"sorted2: {sorted(words.split(), key=str.casefold)}")
    return ' '.join(sorted(words.split(), key=str.casefold))


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
