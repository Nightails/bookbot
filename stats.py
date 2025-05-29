
def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = dict()

    for char in text:
        if char.lower() not in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1

    return characters

def sort_characters(characters_dict):
    sorted_characters = list()
    characters = list(characters_dict)
    for char in characters:
        c = {"char": char, "count": characters_dict[char]}
        sorted_characters.append(c)
    sorted_characters.sort(key=lambda x: x['count'], reverse=True)
    return sorted_characters
