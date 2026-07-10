from src.Validate_Email.utils import validate_email, filter_emails


def test_case_1():

    assert validate_email("lara@hackerrank.com") == True


def test_case_2():

    assert validate_email("lara123@hackerrank.com") == True


def test_case_3():

    assert validate_email("1lara@hackerrank.com") == False


def test_case_4():

    assert validate_email("lara@hackerrank.comm") == False


def test_case_5():

    emails = [
        "lara@hackerrank.com",
        "1abc@gmail.com",
        "abc@yahoo.in",
        "john-doe@gmail.com",
        "@gmail.com"
    ]

    assert filter_emails(emails) == [
        "abc@yahoo.in",
        "john-doe@gmail.com",
        "lara@hackerrank.com"
    ]