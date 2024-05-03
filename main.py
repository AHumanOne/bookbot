def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_words_num_from_text(text)
    print(f'words num is {words_num} in the text')
    letters_dict = get_letters_count_from_text(text)
    print(letters_dict)
    chars_sorted = chars_dict_to_sorted_list(letters_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_num} words found in the document")
    print()

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_num_from_text(text):
    words = text.split()
    return len(words)

def get_letters_count_from_text(text):
    letters_dict = {}
    text = text.lower()
    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] +=1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(letters_dict):
    sorted_list = []
    for ch in letters_dict:
        sorted_list.append({"char": ch, "num": letters_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

