import sys
from stats import get_num_words, get_num_char, pretty_print

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        book_path = sys.argv[1] 
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_path)
    # print(get_num_words(book_text))
    # print(get_num_char(book_text))
    print("============ BOOKBOT ============") 
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    pretty_print(get_num_char(book_text))
    print("============= END ===============")

main()
