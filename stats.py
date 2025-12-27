def get_num_words(book_text):
    num_words = len(book_text.split())

    return f'Found {num_words} total words'

def get_num_chars(book_text):
    book_text = book_text.lower()
    num_chars = {}

    for char in book_text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    return num_chars

def sort_on(dict_list):
    return dict_list["num"]

def sort_dict(num_chars):
    dict_list = [] 
    for key, val in num_chars.items():
        if key.isalpha():
            dict_element = {"char": key, "num": val}
            dict_list.append(dict_element)
    
    dict_list.sort(reverse=True, key=sort_on)
    
    for i in range(len(dict_list)):
        print(f'{dict_list[i]["char"]}: {dict_list[i]["num"]}')
