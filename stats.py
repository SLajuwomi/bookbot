def get_book_word_count(book_text):
    book_text_list = book_text.split()
    return len(book_text_list)


def get_book_char_count(book_text):
    char_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def convert_char_dict_to_list(char_dict):
    final_list = []
    for key in char_dict:
        number = char_dict[key]
        final_list.append({"char": key, "num": number})
    final_list.sort(reverse=True, key=sort_on)
    return final_list
