def get_num_words(text):
    num_words=len(text.split())
    print(f"Found {num_words} total words")

def get_character_count(text):
    char_dict = {}
    for word in text.split():
        for char in word.lower():
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    return_list=[]
    for key in dictionary:
        return_list.append(
            {"char": key,
             "num": dictionary[key]})
    return_list.sort(reverse=True, key=sort_on)
    return return_list
