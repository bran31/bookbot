from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def main():
    path_to_file = "books/frankenstein.txt"
    book = get_book_text(path_to_file)
    # print(book)
    num = count_letters(book)
    letters = repeats(book)
    print(f"{num} words found in the document")
    print(letters)
main()