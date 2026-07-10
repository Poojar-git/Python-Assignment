import re


def validate_email(email):

    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

    return bool(re.match(pattern, email))


def filter_emails(emails):

    return sorted(list(filter(validate_email, emails)))