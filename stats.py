def count_words(inputString):
    words = inputString.split()
    return len(words)

def tally_letters(inputString):
    letter_dict = {}
    
    words = inputString.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def on_tally_sort(tally):
    return tally["count"]


def sort_tally(letter_dict):
    sorted_tally = []
    index = 0
    for letter in letter_dict:
        sorted_tally.append({
            "char": letter,
            "count": letter_dict[letter]
        })

    sorted_tally.sort(key=on_tally_sort, reverse=True)
    return sorted_tally