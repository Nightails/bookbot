
def get_book_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents

def count_words(contents):
    words = contents.split()
    return len(words)

def main():
    words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()

