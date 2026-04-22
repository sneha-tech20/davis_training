import re

def extract_emails(filename):
    with open(filename, 'r') as f:
        text = f.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    return set(emails)  # unique emails