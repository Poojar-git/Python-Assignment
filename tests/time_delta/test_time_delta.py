from src.Time_Delta.utils import time_delta


def test_case_1():

    assert time_delta(
        "Sun 10 May 2015 13:54:36 -0700",
        "Sun 10 May 2015 13:54:36 -0000"
    ) == "25200"


def test_case_2():

    assert time_delta(
        "Sat 02 May 2015 19:54:36 +0530",
        "Fri 01 May 2015 13:54:36 -0000"
    ) == "88200"


def test_case_3():

    assert time_delta(
        "Mon 01 Jan 2024 00:00:00 +0000",
        "Mon 01 Jan 2024 00:00:00 +0000"
    ) == "0"


def test_case_4():

    assert time_delta(
        "Tue 31 Dec 2024 23:59:59 +0000",
        "Wed 01 Jan 2025 00:00:00 +0000"
    ) == "1"


def test_case_5():

    assert time_delta(
        "Fri 15 Aug 1947 00:00:00 +0530",
        "Thu 14 Aug 1947 18:30:00 +0000"
    ) == "0"