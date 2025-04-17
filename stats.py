
def get_num_words(file_contents):

    words = file_contents.split()

    count = len(words)

    return count

def get_count_characters(file_contents):

    characters = list(file_contents)
    dic_char = {}
    
    for character in characters:
        
        character = character.lower()

        if character in dic_char:

            dic_char[character] += 1

        else:

            dic_char[character] = 1

    return (dic_char)

def sort_on(d):

    return d["num"]


def chars_dic_to_sorted_list(dic_char):

    sorted_list = []

    for char in dic_char:

        sorted_list.append({"char":char, "num":dic_char[char]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list