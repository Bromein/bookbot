def get_word_count(book_content):
    word_list = book_content.split()
    return len(word_list)

def count_character_match(book_content):
    lower_cased = book_content.lower()
    char_matches = {}

    for letter in lower_cased:
        if letter in char_matches:
            char_matches[letter] += 1
        else:
            char_matches[letter] = 1
        
    return char_matches
        

def sorted_char_count(char_counts):

    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})

    sorted_list.sort(key=lambda item: item["count"], reverse=True)


    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")


    return sorted_list