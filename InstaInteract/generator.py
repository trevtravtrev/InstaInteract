"""
generator.py generates a comment list (every permutation) from one word/phrase text file and one unicode emoji text file

Inputs: 1. text file of words/phrases 2. text file of unicode emojis (ex: \u2714)
Output: prints new comment list to console (copy and paste it in config.comments)
"""

import itertools


def get_words(filename):
    with open(filename) as f:
        word_list = f.read().splitlines()
    return word_list


def get_emojis(filename):
    emoji_list = []
    with open(filename) as f:
        emojis = f.read().splitlines()
        for emoji in emojis:
            decoded_emoji = emoji.encode().decode('unicode_escape')
            emoji_list.append(decoded_emoji)
    return emoji_list


def create_permutations(words, emojis, emoji_len, word_emoji_len, emoji_perm_len=2):
    permutations = []
    # add all words
    for word in words:
        permutations.append(word)

    # add all permutations of same emoji to same emoji*emoji_len
    for emoji in emojis:
        for i in range(emoji_len):
            permutations.append(emoji*(i+1))

    # add all permutations of word + emoji*word_emoji_len
    for word_emoji_set in itertools.product(words, emojis):
        word_emoji_string = ' '.join(word_emoji_set)
        emoji_stripped_sting = word_emoji_string[:-1]
        emoji = word_emoji_string[-1]
        for i in range(word_emoji_len):
            permutations.append(emoji_stripped_sting+(emoji*(i+1)))

    # add all permutations of unique emoji combinations of emoji_perm_len (recommended value below <3)
    for permutation in list(itertools.permutations(emojis, emoji_perm_len)):
        emoji_str = ''.join(permutation)
        permutations.append(emoji_str)

    print(permutations)
    print(f'length: {len(permutations)}')


def main():
    # settings
    words_file = "words.txt"
    emojis_file = "emojis.txt"

    # main routine
    words = get_words(words_file)
    emojis = get_emojis(emojis_file)
    
    create_permutations(words, emojis, 10, 2, 2)
    # copy the output list to config.comments


if __name__ == '__main__':
    main()
