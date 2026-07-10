def text_alignment(thickness):

    result = []

    # Top Cone
    for i in range(thickness):
        result.append(
            (('H' * i).rjust(thickness - 1) +
             'H' +
             ('H' * i).ljust(thickness - 1))
        )

    # Top Pillars
    for i in range(thickness + 1):
        result.append(
            ('H' * thickness).center(thickness * 2) +
            ('H' * thickness).center(thickness * 6)
        )

    # Middle Belt
    for i in range((thickness + 1) // 2):
        result.append(
            ('H' * (thickness * 5)).center(thickness * 6)
        )

    # Bottom Pillars
    for i in range(thickness + 1):
        result.append(
            ('H' * thickness).center(thickness * 2) +
            ('H' * thickness).center(thickness * 6)
        )

    # Bottom Cone
    for i in range(thickness):
        result.append(
            (
                (('H' * (thickness - i - 1)).rjust(thickness) +
                 'H' +
                 ('H' * (thickness - i - 1)).ljust(thickness))
            ).rjust(thickness * 6)
        )

    return result