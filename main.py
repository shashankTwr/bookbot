import string
def main():
    path_to_file = "./books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    num_words_book = count_number_of_words(file_contents)
    char_count_dict = frequency_of_characters_in_book(file_contents)
    report(path_to_file, num_words_book, char_count_dict)
    return


def get_book_text(path):
    with open(path)  as file:
        return file.read()


def count_number_of_words(txt):
    return len(txt.split())

def frequency_of_characters_in_book(book_contents):
    lowered_book_contents = book_contents.lower()
    list_of_words_in_book = lowered_book_contents.split(" ")
    my_dict:Dict[str, int] = {}
    for word in list_of_words_in_book:
        for character in word:
            if my_dict.get(character) is None and character in string.ascii_lowercase:
                my_dict[character] = 1
            elif character in string.ascii_lowercase :
                my_dict[character] += 1
    return my_dict

def report(path_to_file,num_words_book,char_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words_book} words found in the document\n")
    for char, frequency in char_count.items():
        print(f"The '{char}' character was found {frequency} times")
    return



main() 