import calendar


def find_day(month, day, year):
    weekday = calendar.weekday(year, month, day)
    return calendar.day_name[weekday].upper()