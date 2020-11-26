"""
generator.py generates a comment list (every permutation) from one text/phrase text file and one unicode emoji text file

Inputs: 1. text file of words/phrases 2. text file of unicode emojis (ex: \u2714)
Output: prints new comment list to console (copy and paste it in config.comments)
"""


def get_words(filename):
    with open(filename) as f:
        word_list = f.read().splitlines()
    return word_list


def get_emojis(filename):
    with open(filename) as f:
        emoji_list = f.read().splitlines()
    return emoji_list


def create_comment_list(words, emojis, max_emojis):
    """
    :param words: word list created from text file of words/phrases by get_words function
    :param emojis: emoji list created from text file of emojis by get_emojis function
    :param max_emojis: create every permutation of comment with 0 to max_emojis amount of emojis for each word/phrase
    :return: list of new comments created
    """
    comment_list = []
    for word in words:
        comment_list.append(word)
        for emoji in emojis:
            for i in range(max_emojis + 1):
                emoji_multiplier = emoji * i
                comment = f'{word} {emoji_multiplier}'
                decoded_comment = comment.encode().decode('unicode_escape')
                comment_list.append(decoded_comment)
    return comment_list


def main():
    # settings
    words_file = "comments.txt"
    emojis_file = "emojis.txt"
    max_emojis = 3

    # main routine
    words = get_words(words_file)
    emojis = get_emojis(emojis_file)
    comments = create_comment_list(words, emojis, max_emojis)
    print(comments)
    # copy the output list to config.comments


if __name__ == '__main__':
    main()
