def get_num_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def get_num(item):
    return item["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []

    for ch, count in char_dict.items():
        sorted_list.append({"char": ch, "num": count})
    
    sorted_list.sort(key=get_num, reverse=True)

    return sorted_list
