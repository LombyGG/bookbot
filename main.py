import sys
from stats import *
# count_words, tally_letters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def print_report(filepath):
    content = get_book_text(f"./{filepath}")
    count = count_words(content)
    letter_dict = tally_letters(content)
    sorted_tally = sort_tally(letter_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in sorted_tally:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["count"]}')
    print("============= END ===============")

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])


main()