
from sys import argv
from stats import get_num_words, get_num_characters, sort_characters

def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents

def print_sorted_characters(sorted_character):
    for char in sorted_character:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        return

    file_path = argv[1]
    book_content = get_book_text(file_path)

    words_count = get_num_words(book_content)
    characters_count = get_num_characters(book_content)
    sorted_characters = sort_characters(characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    print_sorted_characters(sorted_characters)
    print("============= END ===============")

main()
