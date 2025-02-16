import re

# # NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# name = r"^[A-Z][a-z]+\s[A-Z][a-z]+$\."
name_regex = re.compile(r"^[A-Z][a-z]*(?:'[A-Z][a-z]*)?(?:\s[A-Z][a-z]+(?:-[A-Z][a-z]+)?)?$")


# phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$\."
phone_regex = re.compile(r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$")

# email_address = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$\."
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

