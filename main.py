from collections import deque


class WordSet:
    def __init__(self):
        self.subsets = {}
        self.is_leaf = False

    def add(self, word):
        if not word:
            self.is_leaf = True
            return
        first, rest = word[:1], word[1:]
        if first not in self.subsets:
            self.subsets[first] = WordSet()
        self.subsets[first].add(rest)

    def fetch(self, word):
        if not word:
            return True, self.is_leaf
        first, rest = word[:1], word[1:]
        if first in self.subsets:
            return self.subsets[first].fetch(rest)
        else:
            return False, False


def read_words_custom():
    words = WordSet()
    with open('words_alpha.txt', 'r') as f:
        for line in f:
            words.add(line.strip())
    return words


def read_words():
    wordlist = set()
    with open('words_alpha.txt', 'r') as f:
        for line in f:
            wordlist.add(line.strip())
    return wordlist


def build_word_2(original_parts: list):
    queue = deque()
    for part in original_parts:
        if len(part) > 1:
            new_parts = original_parts.copy()
            new_parts.remove(part)
            queue.append((part, new_parts))

    while queue:
        word, parts = queue.popleft()
        for part in parts:
            new_word = word + part
            if new_word in dictionary:
                print(new_word)
            if len(part) > 1:
                new_parts = parts.copy()
                new_parts.remove(part)
                queue.append((new_word, new_parts))


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


def build_word_custom(parts: list, word_so_far: str):
    if not parts:
        return
    for part in parts:
        new_word_so_far = word_so_far + part
        is_branch, is_leaf = dictionary.fetch(new_word_so_far)
        if len(new_word_so_far) > 2 and is_leaf:
            print(new_word_so_far)
        if len(part) > 1 and is_branch:
            new_parts = parts.copy()
            new_parts.remove(part)
            build_word_custom(new_parts, new_word_so_far)


if __name__ == '__main__':
    dictionary = read_words_custom()

    while True:
        print('Enter word parts, separated by spaces, or Q to quit:')
        parts_string = input().lower()
        if parts_string == 'q':
            break
        root_parts = parts_string.split(' ')
        build_word_custom(root_parts, '')
