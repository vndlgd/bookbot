from stats import get_num_words, get_num_chars, print_sorted_chars 
import sys

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path_to_file = sys.argv[1]

  print("============ BOOKBOT ============")
  print(f'Analyzing book found at {path_to_file}')
  print("----------- Word Count ----------")
  print(f'Found {get_num_words(get_book_text(path_to_file))} total words')
  print("--------- Character Count -------")
  print_sorted_chars(get_book_text(path_to_file))
  print("============= END ===============")

if __name__ == "__main__":
  main()
