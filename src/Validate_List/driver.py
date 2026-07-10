from utils import filter_emails

if __name__ == "__main__":

    n = int(input())

    emails = []

    for _ in range(n):
        emails.append(input())

    result = filter_emails(emails)

    print(result)