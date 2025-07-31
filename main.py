import sys
from stats import get_book_word_count
from stats import get_book_char_count
from stats import convert_char_dict_to_list

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    book_word_count = get_book_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    book_char_count = get_book_char_count(book_text)
    sorted_list_of_chars = convert_char_dict_to_list(book_char_count)
    print("--------- Character Count -------")
    for item in sorted_list_of_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

