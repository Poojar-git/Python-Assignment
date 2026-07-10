def happiness(array, set_a, set_b):

    score = 0

    for num in array:

        if num in set_a:
            score += 1

        elif num in set_b:
            score -= 1

    return score