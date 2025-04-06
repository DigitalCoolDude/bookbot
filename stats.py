def get_num_words(file_contents):
    word_arr = file_contents.split()
    return len(word_arr)

def get_num_char(file_contents):
    char_dict = {}
    for char in file_contents:
        char_low = char.lower()
        if char_dict.get(char_low):
            char_dict[char_low]+=1
        else:
            char_dict[char_low] = 1
    return char_dict

def sort_dict(dic):
    filtered_dict = {k: v for k, v in dic.items() if k.isalpha()}
    return dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))
