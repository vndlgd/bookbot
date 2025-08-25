def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_char(book_text):
    char_count = {}
    book_text = book_text.lower()
    book_text = book_text.split()
    for word in book_text:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]
    
def pretty_print(char_count): 
    char_count_list = []
    for key, val in char_count.items():
        my_dict = {}
        my_dict["char"] = key
        my_dict["num"] = val
        char_count_list.append(my_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    for el in char_count_list:
        print(f'{el["char"]}: {el["num"]}')



