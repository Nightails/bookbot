
from stats import get_num_words

def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents

def main():
    words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()
