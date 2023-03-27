def read_words():
    wordlist = set()
    with open('words_alpha.txt', 'r') as f:
        for line in f:
            wordlist.add(line.strip())
    return wordlist


def build_word(parts: list, word_so_far: str):
    if not parts:
        return
    for part in parts:
        new_word_so_far = word_so_far + part
        if len(new_word_so_far) > 12:
            continue
        if len(new_word_so_far) > 2 and new_word_so_far in dictionary:
            print(new_word_so_far)
        if len(part) > 1:
            new_parts = parts.copy()
            new_parts.remove(part)
            build_word(new_parts, new_word_so_far)


if __name__ == '__main__':
    dictionary = read_words()

    while True:
        print('Enter word parts, separated by spaces, or Q to quit:')
        parts_string = input().lower()
        if parts_string == 'q':
            break
        root_parts = parts_string.split(' ')
        build_word(root_parts, '')
