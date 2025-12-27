from stats import get_num_words, get_num_chars, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {book}')
        print("----------- Word Count ----------")
        book_text = get_book_text(book)
        print(get_num_words(book_text))
        print("--------- Character Count -------")

        sort_dict(get_num_chars(book_text))

        print("============= END ===============")

if __name__ == "__main__":
    main()
