def count_letters_in_string(string):
    letter_counts = {}
    string = string.lower()
    for letter in string:
        if letter.isalpha():
            if letter not in letter_counts:
                letter_counts[letter] = 0 
        letter_counts[letter] += 1
    return letter_counts

