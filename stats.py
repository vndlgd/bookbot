def sort_on(dict):
  return dict["count"]

def print_sorted_chars(book_text):
  char_count = get_num_chars(book_text)
  sorted_dict = []
  for key, val in char_count.items():
    if key.isalpha():
      dict_item = {"char": key, "count": val}
      sorted_dict.append(dict_item)
  sorted_dict.sort(reverse=True, key=sort_on)
  for item in sorted_dict:
    print(f'{item["char"]}: {item["count"]}')

def get_num_chars(book_text):
  num_char = {}
  book_text = book_text.split()
  for words in book_text:
    for char in words:
      char = char.lower()
      if char in num_char:
        num_char[char] += 1
      else:
        num_char[char] = 1
  return num_char

def get_num_words(book_text):
  num_words = 0
  book_text = book_text.split()
  for word in book_text:
    num_words += 1
  return num_words
