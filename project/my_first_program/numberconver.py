import re

# Mapping of number words to values
num_words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90
}

# Multipliers
scales = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1_000_000,
    "billion": 1_000_000_000
}

def words_to_number(phrase):
    """Convert a number phrase into an integer."""
    phrase = phrase.lower().replace("-", " ")
    words = phrase.split()
    total = 0
    current = 0

    for word in words:
        if word in num_words:
            current += num_words[word]
        elif word in scales:
            current *= scales[word]
            if scales[word] >= 1000:
                total += current
                current = 0
        elif word == "and":
            continue  # Ignore "and"
        else:
            return None  # Not a valid number phrase
    return total + current

# Example usage
num = 0
raw_input = input("Enter a number: ")
try:
    num = int(float(raw_input))
except:
    sample_text = raw_input
    num = words_to_number(sample_text)
try:
    print(int(num))
except:
    print("that not a number \U0001FAE5")

# Output: I have 123 apples and 2005 oranges.
