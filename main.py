import sys
from stats import *


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book = get_book_text(path_to_file)
    num = count_letters(book)
    letters = repeats(book)
    print(f"Found {num} total words")
    print(letters)
    for key in sorted(letters):
        print("%s: %s" % (key, letters[key]))


main()
