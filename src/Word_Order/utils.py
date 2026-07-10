from collections import OrderedDict


def word_order(words):

    word_dict = OrderedDict()

    for word in words:

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    count = len(word_dict)

    frequency = list(word_dict.values())

    return count, frequency