from itertools import combinations


def probability_of_a(letters, k):

    total = 0
    count = 0

    for item in combinations(letters, k):

        total += 1

        if 'a' in item:
            count += 1

    return round(count / total, 4)